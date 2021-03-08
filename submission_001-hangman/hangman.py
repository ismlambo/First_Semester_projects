#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    f = open(file_name, 'r')
    my_words = f.readlines()
    
    return my_words


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    random_words = random.randint(0, len(words) - 1)
    the_word = words[random_words]
    random_letter = random.randint(0, len(the_word) - 2)
    random_blank = the_word[:random_letter] + '_' + the_word[random_letter+1:]
    print("Guess the word: " + random_blank)

    return the_word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    result = input("Guess the missing letter: ")
    return result


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

