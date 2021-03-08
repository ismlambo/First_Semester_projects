import unittest
from test_base import captured_io
from io import StringIO
import draw


class MyTestCase(unittest.TestCase):
    def test_step1(self):
        with captured_io(StringIO('pyramid\n')) as (out, err):
            shape_param = draw.get_shape()
        output = out.getvalue().strip()
        self.assertEqual('Shape?:', output)
        self.assertEqual('pyramid', shape_param)

        with captured_io(StringIO('\npyramid\n')) as (out, err):
            shape_param = draw.get_shape()
        output = out.getvalue().strip()
        self.assertEqual('Shape?: Shape?:', output)
        self.assertEqual('pyramid', shape_param)

        with captured_io(StringIO('PYRAMid\n')) as (out, err):
            shape_param = draw.get_shape()
        self.assertEqual('pyramid', shape_param)

        # TODO: enable this test to check if only valid shapes allowed as input
        # with captured_io(StringIO('invalid\n')) as (out, err):
        #     shape_param = draw.get_shape()
        # output = out.getvalue().strip()
        # self.assertEqual('Shape?:', output)
        # self.assertEqual(None, shape_param)

        with captured_io(StringIO('1\n')) as (out, err):
            height_param = draw.get_height()
        self.assertEqual(1, height_param)

        with captured_io(StringIO('a\n1\n')) as (out, err):
            height_param = draw.get_height()
        output = out.getvalue().strip()
        self.assertEqual('Height?: Height?:', output)
        self.assertEqual(1, height_param)

    def test_step2(self):
        with captured_io(StringIO('')) as (out, err):
            draw.draw_pyramid(3, False)
        output = out.getvalue()
        self.assertEqual("""  *
 ***
*****
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_pyramid(5, False)
        output = out.getvalue()
        self.assertEqual("""    *
   ***
  *****
 *******
*********
""", output)

    def test_step3(self):
        with captured_io(StringIO('')) as (out, err):
            draw.draw_square(3, False)
        output = out.getvalue()
        self.assertEqual("""***
***
***
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_square(5, False)
        output = out.getvalue()
        self.assertEqual("""*****
*****
*****
*****
*****
""", output)

    def test_step4(self):
        with captured_io(StringIO('')) as (out, err):
            draw.draw_triangle(3, False)
        output = out.getvalue()
        self.assertEqual("""*
**
***
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_triangle(5, False)
        output = out.getvalue()
        self.assertEqual("""*
**
***
****
*****
""", output)

    def test_step5(self):
        with captured_io(StringIO('')) as (out, err):
            draw.draw_triangle(5, True)
        output = out.getvalue()
        self.assertEqual("""*
**
* *
*  *
*****
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_square(5, True)
        output = out.getvalue()
        self.assertEqual("""*****
*   *
*   *
*   *
*****
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_pyramid(3, True)
        output = out.getvalue()
        self.assertEqual("""  *
 * *
*****
""", output)

        with captured_io(StringIO('')) as (out, err):
            draw.draw_pyramid(5, True)
        output = out.getvalue()
        self.assertEqual("""    *
   * *
  *   *
 *     *
*********
""", output)


if __name__ == '__main__':
    unittest.main()
