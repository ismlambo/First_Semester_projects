import unittest
from test_base import captured_io
from io import StringIO
import hangman


class MyTestCase(unittest.TestCase):
    def test_previous(self):
        words = hangman.read_file('tests/test_list.txt')
        self.assertEqual(1, len(words))
        self.assertEqual('abc', words[0])

        hangman.random.randint = lambda a,b: 0

        with captured_io(StringIO('a\n')) as (out, err):
            hangman.select_random_word(['abc'])
            hangman.select_random_letter_from('abc')

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: _bc", output)

    def test_step1(self):
        #Test wrong answer
        with captured_io(StringIO('a\n')) as (out, err):
            hangman.show_answer("z","rocket",1)

        output = out.getvalue().strip()
        self.assertEqual("The word was: rocket\nWrong! Do better next time.", output)

        # Test correct answer
        with captured_io(StringIO('a\n')) as (out, err):
            hangman.show_answer("o","rocket",1)

        output = out.getvalue().strip()
        self.assertEqual("The word was: rocket\nWell done! You are awesome!", output)

    def test_step2(self):
        # Test with blank
        with captured_io(StringIO('\n')) as (out, err):
            filename = hangman.ask_file_name()

        self.assertEqual('short_words.txt', filename)
        output = out.getvalue().strip()
        self.assertEqual("Words file? [leave empty to use short_words.txt] :", output)

        # TEst with actual filename
        with captured_io(StringIO('hello.txt\n')) as (out, err):
            filename = hangman.ask_file_name()

        self.assertEqual('hello.txt', filename)

    def test_run(self):
        hangman.random.randint = lambda a,b: 0
        with captured_io(StringIO('d\n')) as (out, err):
            hangman.run_game('tests/test_list.txt')

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: _bc\nGuess the missing letter: The word was: abc\nWrong! Do better next time.", output)


if __name__ == '__main__':
    unittest.main()
