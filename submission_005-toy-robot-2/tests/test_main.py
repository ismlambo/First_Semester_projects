import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot


class MyTestCase(unittest.TestCase):
    def test_step1_then_off(self):

        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step1_then_off_uppercase(self):
        with captured_io(StringIO('HAL\nOFF\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step1_then_off_camelcase(self):
        with captured_io(StringIO('HAL\nOff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step2_then_wrong_then_off(self):

        with captured_io(StringIO('HAL\nJump up\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I did not understand 'Jump up'.
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step3_help_then_off(self):

        with captured_io(StringIO('HAL\nhelp\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands""", output[:178])

    def test_step5_fwd10_then_off(self):

        with captured_io(StringIO('HAL\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.""", output[:114])

    def test_step5_fwd10_then_off_uppercase(self):

        with captured_io(StringIO('HAL\nFORWARD 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.""", output[:114])

    def test_step6_fwd10_then_off(self):

        with captured_io(StringIO('HAL\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step6_fwd0_then_off(self):
        with captured_io(StringIO('HAL\nforward 0\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 0 steps.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step7_back10_then_off(self):

        with captured_io(StringIO('HAL\nback 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step8_right_then_off(self):

        with captured_io(StringIO('HAL\nright\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step8_right_then_fwd10_then_off(self):

        with captured_io(StringIO('HAL\nright\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step8_right_then_back10_then_off(self):

        with captured_io(StringIO('HAL\nright\nback 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step8_right_then_fwd10_then_right_then_fwd5_off(self):

        with captured_io(StringIO('HAL\nright\nforward 10\nright\nforward 5\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (10,0).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (10,-5).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step9_left_then_fwd10_then_off(self):

        with captured_io(StringIO('HAL\nleft\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step9_left_then_back10_then_off(self):

        with captured_io(StringIO('HAL\nleft\nback 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step9_left_then_fwd10_then_left_then_fwd5_off(self):

        with captured_io(StringIO('HAL\nleft\nforward 10\nleft\nforward 5\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (-10,0).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-10,-5).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step10_fwd201_then_fwd10_then_off(self):

        with captured_io(StringIO('HAL\nforward 201\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step10_left_then_fwd101_then_off(self):

        with captured_io(StringIO('HAL\nleft\nforward 101\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_step11_sprint5_then_off(self):

        with captured_io(StringIO('HAL\nsprint 5\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_unittest_exist(self):
        import test_robot
        self.assertTrue('test_robot' in sys.modules, "test_robot module should be found")

    def test_unittest_succeeds(self):
        import test_robot
        test_result = run_unittests("test_robot")
        self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")


if __name__ == '__main__':
    unittest.main()
