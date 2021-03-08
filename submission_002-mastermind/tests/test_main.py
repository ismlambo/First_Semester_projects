import unittest
from test_base import captured_io
from io import StringIO
import mastermind

random_index = 0


def mock_next_random_int():
    global random_index

    random_index += 1
    if random_index == 1:
        return 1
    elif random_index == 2:
        return 2
    elif random_index == 3:
        return 3
    else:
        return 4


class MyTestCase(unittest.TestCase):
    def test_correct(self):
        global random_index
        random_index = 0
        mastermind.random.randint = lambda a, b: mock_next_random_int()

        with captured_io(StringIO('1234\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! You are a codebreaker!
The code was: 1234""", output)

    def test_too_long(self):
        global random_index
        random_index = 0
        mastermind.random.randint = lambda a, b: mock_next_random_int()

        with captured_io(StringIO('12345\n1234\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! You are a codebreaker!
The code was: 1234""", output)

    def test_too_short(self):
        global random_index
        random_index = 0
        mastermind.random.randint = lambda a, b: mock_next_random_int()

        with captured_io(StringIO('123\n1234\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! You are a codebreaker!
The code was: 1234""", output)

    def test_2_turns(self):
        global random_index
        random_index = 0
        mastermind.random.randint = lambda a, b: mock_next_random_int()

        with captured_io(StringIO('5678\n1234\n')) as (out, err):
            mastermind.run_game()

        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: Number of correct digits in correct place:     0
Number of correct digits not in correct place: 0
Turns left: 11
Input 4 digit code: Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0
Congratulations! You are a codebreaker!
The code was: 1234""", output)


if __name__ == '__main__':
    unittest.main()
