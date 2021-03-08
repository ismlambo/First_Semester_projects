import unittest
from test_base import captured_output
#import solution.robot as robot
import robot


class MyTestCase(unittest.TestCase):
    def test_correct(self):

        with captured_output() as (out, err):
            robot.move()

        output = out.getvalue().strip()

        file = open('tests/test_output.txt', 'r')
        expectedOutput = file.read()

        self.assertEqual(expectedOutput, output)


if __name__ == '__main__':
    unittest.main()
