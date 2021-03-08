import random



def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))

def the_input_numbers():
    return input("Input 4 digit code: ")
    
def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """
    answer = the_input_numbers()
    while True:
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            answer = the_input_numbers()
            continue
        else:
            break
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    correct_digits = (correct_digits_and_position, correct_digits_only)
    
    return correct_digits


def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """Checks correctness of answer and show output to user"""


    if correct_digits_and_position == 4:
        correct = True
        return True
    else:
        correct = False
        return False
    return correct


def run_game():
    """Main function for running the game"""

    correct = False

    code = create_code()
    #print(code)
    show_instructions()
    
    turns = 0
    while not correct and turns < 12:
        correct_digits_and_position1 = take_turn(code)
        correct_digits_and_position = correct_digits_and_position1[0]
        correct_digits_only = correct_digits_and_position1[1]
        turns += 1
        correct = check_correctness(turns, correct_digits_and_position)
        show_results(correct_digits_and_position, correct_digits_only)
        if correct_digits_and_position != 4:
            print('Turns left: ' + str(12 - turns))
    
    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')

    show_code(code)


if __name__ == "__main__":
    run_game()
