
valid_commands = ["replay"]
history = ["forward", "right", "back"]

def input_func():
    return input("please enter a replay command: ")
    
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

    return list(filter(lambda x: x != '', split(" ,.;?", text.lower())))

def check_valid_command(listed_command):
    if listed_command[0] == valid_commands[0]:
        return True
    else:
        return False

def do_replay(robot_name, listed_command, user_command):
    global history
    
    silent = False
    if len(listed_command) > 1:
        n = len(history)
        m = 0
        if "-" in listed_command[1]:
            args = listed_command[1].replace('-',' ').split(' ')
            n = args
            if len(args) > 1:
                if args[1].isdigit():
                    n = args[0]
                    m = args[1]
                else:
                    return True, " > "+robot_name+" Sorry, I did not understand '"+user_command+"'."
    
        if 'silent' in listed_command:
            print("silenced")
            silent = True
        
        if 'reversed' in listed_command:
            replay_commands = [replay_command for replay_command in history if replay_command != 'off' or replay_command != 'help' or replay_command != 'history' or replay_command != 'replay']
            replay_commands = replay_commands[::-1]
            
        count_replayed_commands = 0
        for command in replay_commands:
            
            
            if command == 'forward':
                print("forwarded")
                #(do_next, command_output) = do_forward(robot_name, int(arg))
            elif command == 'back':
                print("back")
                #(do_next, command_output) = do_back(robot_name, int(arg))
            elif command == 'right':
                print("right")
                #(do_next, command_output) = do_right_turn(robot_name)
            elif command == 'left':
                print("left")
                #(do_next, command_output) = do_left_turn(robot_name)
            elif command == 'sprint':
                print("left")
                #(do_next, command_output) = do_sprint(robot_name, int(arg))
                
            count_replayed_commands += 1
        
        if silent == True:
            replay_feedback = " > "+robot_name+" replayed "+str(count_replayed_commands)+" commands silently."
        elif count_replayed_commands == 1 and silent == True:
            replay_feedback = " > "+robot_name+" replayed "+str(count_replayed_commands)+" command silently."
        elif count_replayed_commands == 1:
            replay_feedback = " > "+robot_name+" replayed "+str(count_replayed_commands)+" command."
        else:
            replay_feedback = " > "+robot_name+" replayed "+str(count_replayed_commands)+" commands."

    return True, replay_feedback

def robot_start():

    while True:
        user_command = input_func()
        listed_command = convert_to_word_list(user_command)
        valid = check_valid_command(listed_command)
        if valid == True:
            do_replay("robot_name", listed_command, user_command)
            return False
        else:
            print("sorry")

if __name__ == "__main__":
    robot_start()