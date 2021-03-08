import unittest
from test_base import captured_io
from io import StringIO
import hangman


class MyTestCase(unittest.TestCase):

    def test_step1(self):
        # test random_fill_word
        for i in range(0,1000):
            filled_word = hangman.random_fill_word("abcde")
            self.assertEqual(5, len(filled_word.split('_')))

        # test is_missing_char
        self.assertTrue(hangman.is_missing_char('abc', 'a__', 'b'))
        self.assertFalse(hangman.is_missing_char('abc', 'a__', 'a'))
        self.assertFalse(hangman.is_missing_char('abc', 'a__', 'f'))

        # test fill_in_char
        self.assertEqual('ab_', hangman.fill_in_char('abc', 'a__', 'b'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'a'))
        self.assertEqual('a__', hangman.fill_in_char('abc', 'a__', 'f'))

    def test_step2(self):
        with captured_io(StringIO('a\nb\n')) as (out, err):
            hangman.run_game_loop('abc',"__c")

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: __c\nGuess the missing letter: a_c\nGuess the missing letter: abc", output)

        with captured_io(StringIO('f\na\nb\n')) as (out, err):
            hangman.run_game_loop('abc',"__c")

        output = out.getvalue().strip()
        self.assertEqual("""Guess the word: __c
Guess the missing letter: Wrong! Number of guesses left: 4""", output[:78])
        self.assertEqual("Guess the missing letter: a_c\nGuess the missing letter: abc", output[-59:])

    def test_step3(self):
        with captured_io(StringIO('exit\n')) as (out, err):
            hangman.run_game_loop('abc',"__c")

        output = out.getvalue().strip()
        self.assertEqual("Guess the word: __c\nGuess the missing letter: Bye!", output)

    def test_step4(self):
        with captured_io(StringIO('z\nx\ny\nw\nq\n')) as (out, err):
            hangman.run_game_loop('abc',"__c")

        output = out.getvalue().strip()
        self.assertEqual("""Guess the word: __c
Guess the missing letter: Wrong! Number of guesses left: 4""", output[:78])
        self.assertEqual('Sorry, you are out of guesses. The word was: abc', output[-48:])

    def test_step5_all_left(self):
        with captured_io(StringIO('')) as (out, err):
            hangman.draw_figure(4)
        output = out.getvalue().strip()
        self.assertEqual("""/----
|
|
|
|
_______""", output)

    def test_step5_none_left(self):
        with captured_io(StringIO('')) as (out, err):
            hangman.draw_figure(0)
        output = out.getvalue().strip()
        self.assertEqual("""/----
|   0
|  /|\\
|   |
|  / \\
_______""", output)


if __name__ == '__main__':
    unittest.main()
