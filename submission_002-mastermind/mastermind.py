import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")

    code = []
    while len(code) != 4:
        value = random.randint(1, 8)
        if value not in code:
            code.append(value)
    code_str = str(code)

    turn_left = 12
    while True:
        
        #getting user input
        count_corrects = 0
        count_wrongs = 0

        guess = input("Input 4 digit code: ")
        if len(guess) > 4 or len(guess) < 4:
            print("Please enter exactly 4 digits.")
            continue
        if guess.isdigit() == False:
            print("Please enter exactly 4 digits.")
            continue

        #check the code in correct place
        if guess[0] == code_str[1]:
            count_corrects += 1
        if guess[1] == code_str[4]:
            count_corrects += 1
        if guess[2] == code_str[7]:
            count_corrects += 1
        if guess[3] == code_str[10]:
            count_corrects += 1
        print("Number of correct digits in correct place:     " + format(count_corrects))

        #check the code not in correct place
        if guess[0] in code_str and guess[0] != code_str[1]:
            count_wrongs += 1
        if guess[1] in code_str and guess[1] != code_str[4]:
            count_wrongs += 1
        if guess[2] in code_str and guess[2] != code_str[7]:
            count_wrongs += 1
        if guess[3] in code_str and guess[3] != code_str[10]:
            count_wrongs += 1
        print("Number of correct digits not in correct place: " + format(count_wrongs))

        #if you crack the code
        if count_corrects == 4:
            print("Congratulations! You are a codebreaker!")
            print("The code was: ", end="")
            print(*code, sep="")
            break
        #turns left
        turn_left -= 1
        if turn_left == 0:
            print("The code was: ", end="")
            print(*code, sep="")
            break
        print("Turns left: " + format(turn_left))

if __name__ == "__main__":
    run_game()
