
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


draw_diamond(10, True)