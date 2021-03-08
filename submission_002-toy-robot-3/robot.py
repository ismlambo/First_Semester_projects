
# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'history']
history = []

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)

def convert_to_word_list(text):

    return list(filter(lambda x: x != '', split(" .;?", text.lower())))

def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    global history

    while True:
        prompt = ''+robot_name+': What must I do next? '
        command = input(prompt)

        if command.lower() == "off":
            return ["off"], ["off", 0, command]
        else:
            n = 0
            m = 0
            user_command_list = convert_to_word_list(command.lower())
            if user_command_list[0] in valid_commands:
                if len(user_command_list) == 2:
                    if user_command_list[1].isdigit():
                        n = int(user_command_list[1])
                    return user_command_list, [user_command_list[0], n, command]
                return user_command_list, [user_command_list[0], 0, command]

            elif user_command_list[0] == "replay":

                if len(user_command_list) > 1:
                    n = len(history)
                    m = 0
                    if "-" in user_command_list[1]:
                        args = user_command_list[1].replace('-',' ').split(' ')
                        n = args
                        if len(args) > 1:
                            if args[1].isdigit():
                                n = args[0]
                                m = args[1]
                            else:
                                output(robot_name, "Sorry, I did not understand '"+command+"'.")
                                return get_command(robot_name)
                    else:
                        for i in user_command_list:
                            if i.isdigit() == False and '-' not in i and i != "silent" and i != "reversed" and i != "replay":
                                output(robot_name, "Sorry, I did not understand '"+command+"'.")
                                return get_command(robot_name)
                            
                return user_command_list, [n, m, command]
            
            else:
                output(robot_name, "Sorry, I did not understand '"+command+"'.")
                continue

def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = str(command).split(' ')
    # args = command.replace('-','').split('')
    print(args)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
HISTORY - display the previously executed commands
REPLAY - replay the previously executed commands
REPLAY SILENT - replay the previously executed commands without printing out the output
REPLAY REVERSED - replay the previous executed commands in reverse
REPLAY REVERSED SILENT - replay the previous executed commands in reverse without printing
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps, silent):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        if not silent:
            print(command_output)
        return do_sprint(robot_name, steps - 1, silent)

def do_history(robot_name, command):
    global history
    history.append(command)
    return True, history


def do_replay(robot_name, user_command_list):
    global history
    replay_commands = [replay_command for replay_command in history if replay_command != 'off' or replay_command != 'help' or replay_command != 'history' or replay_command != 'replay']
    silent = False
    reverse = False
    n = 0
    m = 0
    if len(user_command_list) > 1:
        if "-" in user_command_list[1]:
            args = user_command_list[1].replace('-',' ').split(' ')
            n = int(args[0])
            m = -1
            if len(args) > 1:
                if args[1].isdigit():
                    n = int(args[0])
                    m = int(args[1])
        if user_command_list[1].isdigit():
            n = int(user_command_list[1])
    
    if 'silent' in user_command_list:
        silent = True
        
    if 'reversed' in user_command_list:
        reverse = True
        replay_commands = [replay_command for replay_command in history if replay_command != 'off' or replay_command != 'help' or replay_command != 'history' or replay_command != 'replay']
        replay_commands = replay_commands[::-1]
    count_replayed_commands = 0
    played_commands = 0
    history_length = len(history)
    for command in replay_commands:
        command = convert_to_word_list(command)
        command_name = command[0]
        if len(command) > 1:
            arg = command[1]
        else:
            arg = 0

        if m == 0 and n == 0:
            if command_name == 'forward':
                (do_next, command_output) = do_forward(robot_name, int(arg))
                if not silent:
                    print(command_output)
                    show_position(robot_name)

            elif command_name == 'back':
                (do_next, command_output) = do_back(robot_name, int(arg))
                if not silent:
                    print(command_output)
                    show_position(robot_name)

            elif command_name == 'right':
                (do_next, command_output) = do_right_turn(robot_name)
                if not silent:
                    print(command_output)
                    show_position(robot_name)

            elif command_name == 'left':
                (do_next, command_output) = do_left_turn(robot_name)
                if not silent:
                    print(command_output)
                    show_position(robot_name)

            elif command_name == 'sprint':
                (do_next, command_output) = do_sprint(robot_name, int(arg), silent)
                if not silent:
                    print(command_output)
                    show_position(robot_name)            
            played_commands += 1
        if m == 0 and n != 0:
            if count_replayed_commands >= history_length - n:
                if command_name == 'forward':
                    (do_next, command_output) = do_forward(robot_name, int(arg))
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'back':
                    (do_next, command_output) = do_back(robot_name, int(arg))
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'right':
                    (do_next, command_output) = do_right_turn(robot_name)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'left':
                    (do_next, command_output) = do_left_turn(robot_name)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'sprint':
                    (do_next, command_output) = do_sprint(robot_name, int(arg), silent)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)            
                played_commands += 1
        if m != 0 and n != 0:
            if count_replayed_commands >= m-1 and count_replayed_commands + 1 < n:
                if command_name == 'forward':
                    (do_next, command_output) = do_forward(robot_name, int(arg))
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'back':
                    (do_next, command_output) = do_back(robot_name, int(arg))
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'right':
                    (do_next, command_output) = do_right_turn(robot_name)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'left':
                    (do_next, command_output) = do_left_turn(robot_name)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)

                elif command_name == 'sprint':
                    (do_next, command_output) = do_sprint(robot_name, int(arg), silent)
                    if not silent:
                        print(command_output)
                        show_position(robot_name)            
                played_commands += 1
        count_replayed_commands += 1
        
    if silent == True and reverse == False:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" commands silently."
    elif reverse == True and silent == True:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" commands in reverse silently."
    elif reverse == True and silent == False:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" commands in reverse."
    elif count_replayed_commands == 1 and silent == True:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" command silently."
    elif count_replayed_commands == 1:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" command."
    else:
        replay_feedback = " > "+robot_name+" replayed "+str(played_commands)+" commands."

    return True, replay_feedback


def handle_command(robot_name, user_command_list, processed_command_list):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global history
    command_name = processed_command_list[0]
    arg = processed_command_list[1]
    command = processed_command_list[2]
    replay = user_command_list[0]

  

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        do_history(robot_name, command)
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        do_history(robot_name, command)
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        do_history(robot_name, command)
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        do_history(robot_name, command)
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        do_history(robot_name, command)
        silent = False
        (do_next, command_output) = do_sprint(robot_name, int(arg), silent)
    elif replay == 'replay':
        (do_next, command_output) = do_replay(robot_name, user_command_list)
    elif command_name == 'history':
        do_next = True
        command_output = history

    print(command_output)
    show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0

    user_command_list, processed_command_list = get_command(robot_name)
    while handle_command(robot_name, user_command_list, processed_command_list):
        user_command_list, processed_command_list = get_command(robot_name)
     

    history = []
    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
