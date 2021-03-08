

# TODO: Decompose into functions

#-------robot change-direction instructios-----
def move_forward(length):
    print("* Move Forward "+str(length))

def turn_right(degrees):
    print("* Turn Right "+str(degrees)+" degrees")

#instruct the robot move in a square shape or direction
def square_direction():
    size = 10
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        move_forward(size)
        turn_right(degrees)

#instruct the robot move in a rectangular shape or direction
def rectangular_direction():
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        move_forward(length)
        turn_right(degrees)
        move_forward(width)
        turn_right(degrees)

#instruct the robot move in a circular shape or direction
def circular_movement():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        move_forward(length)
        turn_right(degrees)

#instruct the robot move in a square dancing shape or direction
def square_dancing_direction():
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        move_forward(length)
        print("Moving in a square of size 20")
        for j in range(4):
            move_forward(length)
            degrees = 90
            turn_right(degrees)

#instruct the robot move in a square dancing shape or direction
def crop_circular_direction():
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        move_forward(length)
        print("Moving in a circle")
        for k in range(360):
            length = 1
            degrees = 1
            move_forward(length)
            turn_right(degrees)


#the robot will move in a sequence from the top instruction to the bottom
def move():
    '''I would name move() --> robo_turns()
    because the code instructs the robot to make turns in different shapes and sizes'''
    square_direction()
    rectangular_direction()
    circular_movement()
    square_dancing_direction()
    crop_circular_direction()
    
def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
