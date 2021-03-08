import unittest
from test_base import captured_output
from io import StringIO
import course


class MyTestCase(unittest.TestCase):
    def test_step1(self):
        with captured_output() as (out, err):
            course.create_outline()

        output = out.getvalue().strip()
        self.assertEqual("Course Topics:\n*", output[:16])
        self.assertTrue('* Introduction to Python' in output)
        self.assertTrue('* Tools of the Trade' in output)
        self.assertTrue('* How to make decisions' in output)
        self.assertTrue('* How to repeat code' in output)
        self.assertTrue('* How to structure data' in output)
        self.assertTrue('* Functions' in output)
        self.assertTrue('* Modules' in output)

    def test_step2(self):
        with captured_output() as (out, err):
            course.create_outline()

        output = out.getvalue().strip()
        self.assertTrue('Problems:' in output)
        self.assertTrue('* Introduction to Python : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* Tools of the Trade : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* How to make decisions : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* How to repeat code : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* How to structure data : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* Functions : Problem 1, Problem 2, Problem 3' in output)
        self.assertTrue('* Modules : Problem 1, Problem 2, Problem 3' in output)

    def test_step3(self):
        with captured_output() as (out, err):
            course.create_outline()

        output = out.getvalue().strip()
        self.assertTrue('Student Progress:' in output)
        self.assertTrue('1.' in output)
        self.assertTrue('2.' in output)
        self.assertTrue('[GRADED]' in output)
        self.assertTrue('[STARTED]' in output)
        self.assertTrue('[COMPLETED]' in output)

    def test_step4(self):
        with captured_output() as (out, err):
            course.create_outline()

        output = out.getvalue().strip()
        self.assertEqual("""Course Topics:
* Functions
* How to make decisions
* How to repeat code
* How to structure data
* Introduction to Python
* Modules
* Tools of the Trade""", output[:151])

        self.assertTrue(output.index('COMPLETED') > output.index('GRADED'))
        self.assertTrue(output.index('GRADED') > output.index('STARTED'))


if __name__ == '__main__':
    unittest.main()
