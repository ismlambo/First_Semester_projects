#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    file_open = open(file_name,"r") 
    file_read = file_open.readlines()  
    file_open.close()  
    return file_read



def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    index = random.randint(0,len(words)-1)
    word = words[index]   
    
    letter_index = random.randint(0,len(word)-1)
    letter = word[letter_index]
    display_word = word.replace(word[letter_index],"_",1)
    
    print("Guess the word: " +display_word) 
    
    return words[index]





def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    user_input = input("Guess the missing letter: ")
    answer = user_input
    return answer


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

