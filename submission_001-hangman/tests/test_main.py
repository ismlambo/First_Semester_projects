import unittest
from test_base import captured_io, captured_output
from io import StringIO
import hangman


class MyTestCase(unittest.TestCase):
    def test_step1(self):
        words = hangman.read_file('tests/test_list.txt')
        self.assertEqual(2, len(words))
        self.assertEqual('abc\n', words[0])
        self.assertEqual('def', words[1])

    def test_step2(self):
        hangman.random.randint = lambda a,b: 0

        with captured_io(StringIO('a\n')) as (out, err):
            hangman.select_random_word(['abc'])

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: _bc", output)

    def test_step3(self):
        with captured_io(StringIO('a\n')) as (out, err):
            hangman.get_user_input()

        output = out.getvalue().strip()
        self.assertEqual("Guess the missing letter:", output)

    def test_step4(self):
        hangman.random.randint = lambda a, b: 0

        with captured_io(StringIO('a\n')) as (out, err):
            hangman.run_game('tests/test_list.txt')

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: _bc\n\nGuess the missing letter: The word was: abc", output)


if __name__ == '__main__':
    unittest.main()
