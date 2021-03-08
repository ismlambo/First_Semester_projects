

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
        shape = input("Shape?: ")
        shape = shape.lower()
        if len(shape) == 0:
            continue
        if shape == 'pyramid' or shape == 'square' or shape == 'triangle' or shape == 'rectangle' or shape == 'diamond' or shape == 'corn':
            break
        
    return shape

# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        my_height = input("Height?: ")
        if not my_height.isdigit():
            continue
        if len(my_height) == 0:
            continue
        if int(my_height) > 0 and int(my_height) < 80:
            break
        else:
            continue
    return int(my_height)


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == False:
        stars = 1
        space = height
        while height > 0:
            print(" "*(space-1)+"*"*(stars))
            stars += 2
            space -= 1
            height = height -1

    elif outline == True:
        y_axis = 0
        space = height
        inner_space = 1
        while y_axis <= height:
            #first star
            if y_axis == 1:
                print(" "*(space)+"*")
                
            #second step
            elif y_axis > 1 and y_axis < height:
                print(" "*(space)+"*"+" "*inner_space+"*")
                
                inner_space += 2
            #base 
            elif y_axis == height:
                print("*" + "*" * inner_space + "*")
                
            space -= 1
            y_axis += 1


# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        space = height - 1
        for i in range(1,height+1):
            print("*"*(space+1))
    elif outline == True:
        for y_axis in range(height):
            for x_axis in range(height):
                if y_axis==0 or y_axis==height-1  or x_axis==0 or x_axis==height-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for y_axis in range(1, (height + 1)):
            for x_axis in range(1,y_axis+1):
                print("*",end="")
            print()

    elif outline == True:
        y_axis = 1
        space = 1
        stars = 1
        while y_axis <= height:
            if y_axis <= 2:
                print("*"*stars)
            elif y_axis > 2 and y_axis < height:
                print("*"+" "*(space)+"*")
                space += 1
            elif y_axis == height:
                print("*"*y_axis)
            stars += 1
            y_axis += 1

def draw_rectangle(height, outline):
    if outline == False:
        y_axis = 1
        width = height * 2
        
        while y_axis <= height:
            print("*"*width)
            y_axis += 1    

    elif outline == True:
        y_axis = 1
        width = height * 2
        while y_axis <= height:
            if y_axis == 1 or y_axis == height:
                print("*"*width)
            elif y_axis > 1 or y_axis < height:
                print("*"+" "*(width-2)+"*")
            y_axis += 1

def draw_diamond(height, outline):
    if outline == False:
        if height%2 != 0:
            this_height = height
        else:
            this_height = height + 1
        half_height = int((this_height/2)+0.5)
        y_axis = 1
        stars = 1
        upper_space = half_height - 1
        after_space = 1
        while y_axis <= this_height:
            if y_axis <= half_height:
                print(" "*(upper_space)+"*"*(stars))
                stars += 2
                upper_space -= 1
            elif y_axis == (half_height + 1):
                spacess = stars - 4                
                print(" "*after_space + "*"*spacess)
                spacess -= 2
                after_space += 1
            elif y_axis > (half_height + 1):
                print(" "*after_space + "*"*spacess)
                spacess -= 2
                after_space += 1
            y_axis += 1

    elif outline == True:
        if height%2 != 0:
            this_height = height
        else:
            this_height = height + 1
        half_height = int((this_height/2)+0.5)
        y_axis = 1
        stars = 1
        upper_space = half_height - 1
        after_space = 1
        while y_axis <= this_height:
            if y_axis == 1:
                print(" "*upper_space+"*")
                upper_space -= 1
            if y_axis > 1 and y_axis <= half_height:
                print(" "*(upper_space)+"*"+" "*(stars)+"*")
                stars += 2
                upper_space -= 1
            elif y_axis == (half_height + 1):
                spacess = stars - 4                
                print(" "*after_space + "*"+" "*(spacess)+"*")
                spacess -= 2
                after_space += 1
            elif y_axis > (half_height + 1) and y_axis < this_height:
                print(" "*after_space + "*"+" "*(spacess)+"*")
                spacess -= 2
                after_space += 1
            elif y_axis == (this_height):
                print(" "*after_space + "*")
            y_axis += 1
def draw_corn(height, outline):
    if outline == False:
        space = 0
        while height > 0:
            print(" "*space+"*"*(2*height-1))
            space += 1
            height -= 1

    elif outline == True:
        top = height
        space = 0
        while height > 0:
            if height == top:
                print("*"*(2*height-1))
            elif height < top and height > 1:
                print(" "*space+"*"+" "*((2*height-1)-2)+"*")
            elif height == 1:
                print(" "*space+"*")
            space += 1
            height -= 1
# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'diamond':
        draw_diamond(height, outline)
    elif shape == 'corn':
        draw_corn(height, outline) 


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        outline = input("Outline only? (y/N): ")

        if outline == 'y':
            return True
        elif outline == 'n':
            return False
        elif len(outline) == 0:
            continue
        else:
            continue


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

