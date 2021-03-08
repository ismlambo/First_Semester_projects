import re

def get_robotName():
    """The user is asked to provide an alias for the robot that will
    be used throughout the run of the programme"""

    robotName = input("What do you want to name your robot? ")

    print(robotName + ": ",end="")
    print("Hello kiddo!")
    return robotName

def robot_await_commands(robotName):
    """
    we will get the commands from the user as one(1) input.
    --------------
    next we will seperate the strings and numbers
    in order to get the command and the value of steps that
    the robot has to move by
    --------------
    """
    while True:
        print(robotName + ": ",end="")
        command = input("What must I do next? ")

        command_name = "".join(re.split("[^a-zA-Z]*", command.lower()))
        command_value = "".join(re.split("[^0-9]*", command))
        
        if command_name == "" or command == "":
            print("Sorry, I did not understand ", "'"+command+"'")
            continue

        elif command_value == "":
            command_value = 0
            full_command = (command_name, command_value, command)
            return full_command

        elif command_name != "" and command_value != "":
            full_command = (command_name, command_value, command)
            return full_command
        
        else:
            print(robotName + ": ",end="")
            print("Sorry, I did not understand", "'",command,"'.")
            continue

def check_terminate(command_name, robotName):
    """The robot will shut down immediately if the user enters "OFF" as a command"""
    if command_name == "off":
        print(robotName + ": ",end="")
        print("Shutting down..")
        return True
    else:
        return False

def process_command(command_name, command_value, command, robotName, coordinates):
    """At this point, we evaluate the commands is they exist in the robot's database 
    and we then call the function that is responsible for that command, if it exists.
    Here we also alert the user if the command entered is not understood by the robot."""
    valid_commands = ["off", "help","forward", "back", "right", "left", "sprint"]
    original_command_value = 0
    sprint_value = 0
    x_axis = coordinates[0]
    y_axis = coordinates[1]
    robot_direction = coordinates[2]
    temp_coordinates = (x_axis,y_axis)
    """
    robot-map/direction in detail:
                0
                |
            3---o---1
                |
                2
    """
    #print(command_name, command_value, command)
    if command_name not in valid_commands:
        print(robotName + ": ",end="")
        print("Sorry, I did not understand", "'"+command+"'.")
    else:
        if command_name == "help":
            help()

        elif command_name == "forward":
            temp_coordinates = robot_move_forward(command_value, robotName, x_axis, y_axis, robot_direction)
            
        elif command_name == "back":
            temp_coordinates = robot_move_back(command_value, robotName, x_axis, y_axis, robot_direction)
            
        elif command_name == "right":
            robot_direction = robot_turn_right(robotName, robot_direction, x_axis, y_axis)
            
        elif command_name == "left":
            robot_direction = robot_turn_left(robotName, robot_direction, x_axis, y_axis)
            
        elif command_name == "sprint":
            original_command_value = command_value
            temp_coordinates = robot_sprint(command_value, sprint_value, robotName, x_axis, y_axis, robot_direction, original_command_value)
            sprint_value = 0
            
    coordinates = (temp_coordinates[0], temp_coordinates[1], robot_direction)
    return coordinates

def robot_sprint(command_value, sprint_value, robotName, x_axis, y_axis, robot_direction, original_command_value):
    """The robot must sprint or move forward faster than normal"""

    if command_value == 0:
        if robot_direction == 0:
            if y_axis + sprint_value > 200:
                print(robotName + ": ",end="")
                print("Sorry, I cannot go outside my safe zone.")
            else:
                y_axis = y_axis + sprint_value
                for i in range(original_command_value):
                    print(" > " + robotName + " moved forward by " + str(original_command_value) + " steps.")
                    original_command_value -= 1
        elif robot_direction == 1:
            if x_axis + sprint_value > 100:
                print(robotName + ": ",end="")
                print("Sorry, I cannot go outside my safe zone.")
            else:
                x_axis = x_axis + sprint_value
                for i in range(original_command_value):
                    print(" > " + robotName + " moved forward by " + str(original_command_value) + " steps.")
                    original_command_value -= 1
        elif robot_direction == 2:
            if y_axis - sprint_value < -200:
                print(robotName + ": ",end="")
                print("Sorry, I cannot go outside my safe zone.")
            else:
                y_axis = y_axis - sprint_value
                for i in range(original_command_value):
                    print(" > " + robotName + " moved forward by " + str(original_command_value) + " steps.")
                    original_command_value -= 1
        elif robot_direction == 3:
            if x_axis - sprint_value < -100:
                print(robotName + ": ",end="")
                print("Sorry, I cannot go outside my safe zone.")
            else:
                x_axis = x_axis - sprint_value
                for i in range(original_command_value):
                    print(" > " + robotName + " moved forward by " + str(original_command_value) + " steps.")
                    original_command_value -= 1
        
        coordinates = (x_axis,y_axis)
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
        return coordinates
 
    else:
        sprint_value = sprint_value + command_value
        return robot_sprint((command_value - 1), sprint_value, robotName, x_axis, y_axis, robot_direction, original_command_value)

def robot_turn_left(robotName, robot_direction, x_axis, y_axis):
    """From the direction at which the robot is facing, this fucntion will allow
    it to turn 90 degrees anti-clockwise."""

    if robot_direction == 0:
        robot_direction = 3
    elif robot_direction == 1:
        robot_direction = 0
    elif robot_direction == 2:
        robot_direction = 1
    elif robot_direction == 3:
        robot_direction = 2

    print(" > " + robotName + " turned left.")
    print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
    return robot_direction

def robot_turn_right(robotName, robot_direction, x_axis, y_axis):
    """Robot must turn exactly 90 degrees from the direction that
    it is currently facing""" 

    if robot_direction == 0:
        robot_direction = 1
    elif robot_direction == 1:
        robot_direction = 2
    elif robot_direction == 2:
        robot_direction = 3
    elif robot_direction == 3:
        robot_direction = 0

    print(" > " + robotName + " turned right.")
    print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
    return robot_direction

def help():
    """A list of instructions that the robot can understand are provided
    with respective explainations on how they will affect the state of 
    the robot and allow interaction with the user.
    ----------
    tips on how to improve the interaction between the user and the robot
    are provided below"""

    print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - Move robot on a forward direction by a certain number of steps.
           robot can only move within -200 to 200 on the y-axis.
           robot can only move within -100 to 100 on the x-axis.
BACK    - Move robot on a backward direction by a certain number of steps.
RIGHT   - Turns robot clockwise by only 90 degrees.
LEFT    - Turns robot to by 90 degrees anti-clockwise.
SPRINT  - Move the robot forward by the sum of the steps as they decrease
           by one(1) value after each addition. Hence described as sprinting.

Provide integer values after "FORWARD", "BACK" and "SPRINT" to represent the
number of steps at which you want the robot to move by.
     """)

    pass

def robot_move_forward(command_value, robotName, x_axis, y_axis, robot_direction):
    """robot will move forward by a certain number of steps and 
    taking into account the limit of movement:
        y-axis(-200 - 200)
        x-axis(-100 - 100)"""

    if robot_direction == 0:
        y_axis = y_axis + command_value
    elif robot_direction == 1:
        x_axis = x_axis + command_value
    elif robot_direction == 2:
        y_axis = y_axis - command_value
    elif robot_direction == 3:
        x_axis = x_axis - command_value


    #-----------------
    """this part will manage the limit area at which the robot will move"""
    if y_axis > 200 or y_axis < -200:
        if y_axis > 200:
            y_axis = y_axis - command_value
        else:
            y_axis = y_axis + command_value
        coordinates = (x_axis,y_axis)
        print(robotName + ": ",end="")
        print("Sorry, I cannot go outside my safe zone.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")

    elif x_axis > 100 or x_axis < -100:
        if x_axis > 200:
            x_axis = x_axis - command_value
        else:
            x_axis = x_axis + command_value
        coordinates = (x_axis,y_axis)
        print(robotName + ": ",end="")
        print("Sorry, I cannot go outside my safe zone.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
    #-----------------
    else:
        coordinates = (x_axis,y_axis)
        print(" > " + robotName + " moved forward by " + str(command_value) + " steps.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
    
    return coordinates

def robot_move_back(command_value, robotName, x_axis, y_axis, robot_direction):
    """robot will move backward by a certain number of steps and 
    taking into account the limit of movement:
        y-axis(-200 - 200)
        x-axis(-100 - 100)"""

    if robot_direction == 0:
        y_axis = y_axis - command_value
    elif robot_direction == 1:
        x_axis = x_axis - command_value
    elif robot_direction == 2:
        y_axis = y_axis + command_value
    elif robot_direction == 3:
        x_axis = x_axis + command_value

    
    #-----------------
    """this part will manage the limit area at which the robot will move"""
    if y_axis > 200 or y_axis < -200:
        if y_axis > 200:
            y_axis = y_axis - command_value
        else:
            y_axis = y_axis + command_value
        coordinates = (x_axis,y_axis)
        print(robotName + ": ",end="")
        print("Sorry, I cannot go outside my safe zone.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")

    elif x_axis > 100 or x_axis < -100:
        if x_axis > 200:
            x_axis = x_axis - command_value
        else:
            x_axis = x_axis + command_value
        coordinates = (x_axis,y_axis)
        print(robotName + ": ",end="")
        print("Sorry, I cannot go outside my safe zone.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")
    #-----------------
    else:
        coordinates = (x_axis,y_axis)
        print(" > " + robotName + " moved back by " + str(command_value) + " steps.")
        print(" > " + robotName + " now at position (" + str(x_axis) +","+str(y_axis) + ").")

    return coordinates

def robot_start():
    """This is the entry function, do not change
    ------------------
    this fucntion acts as the control or main fucntion that provides
    the correct order at which the procesessing of robot function 
    must occur"""
    
    robotName = get_robotName()
    terminate = False
    coordinates = (0,0,0)

    while not terminate: 
        full_command = robot_await_commands(robotName)
        command_name = full_command[0]
        command_value = int(full_command[1])
        command = full_command[2]
        terminate = check_terminate(command_name, robotName)
        coordinates = process_command(command_name, command_value, command, robotName, coordinates)

    pass

if __name__ == "__main__":
    robot_start()