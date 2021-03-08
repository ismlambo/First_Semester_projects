import unittest
import sys
from test_base import run_unittests
import super_algos


class MyTestCase(unittest.TestCase):
    def test_step1_find_min_empty(self):
        result = super_algos.find_min([])
        self.assertEqual(-1, result)

    def test_step1_find_min_normal(self):
        result = super_algos.find_min([3,5,6,1,10])
        self.assertEqual(1, result)

    def test_step1_find_min_one_element(self):
        result = super_algos.find_min([3])
        self.assertEqual(3, result)

    def test_step1_find_min_negative(self):
        result = super_algos.find_min([3,100,-101,4,-5])
        self.assertEqual(-101, result)

    def test_step1_find_min_invalid_elements(self):
        result = super_algos.find_min(['a',100,'b',4,-5])
        self.assertEqual(-1, result)

    def test_step2_sum_all_empty(self):
        result = super_algos.sum_all([])
        self.assertEqual(-1, result)

    def test_step2_sum_all_normal(self):
        result = super_algos.sum_all([1,2,3,4,5])
        self.assertEqual(15, result)

    def test_step2_sum_all_one_element(self):
        result = super_algos.sum_all([3])
        self.assertEqual(3, result)

    def test_step2_sum_all_negative(self):
        result = super_algos.sum_all([-1,-2,-3])
        self.assertEqual(-6, result)

    def test_step2_sum_all_invalid_elements(self):
        result = super_algos.sum_all(['a',100,'b',4,-5])
        self.assertEqual(-1, result)

    def test_step3_find_strings_one(self):
        results = super_algos.find_possible_strings(['a','b','c','d'], 1)
        self.assertEqual(['a','b','c','d'], results)

    def test_step3_find_strings_three(self):
        result = super_algos.find_possible_strings(['a','b'], 3)
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], result)

    def test_step3_find_strings_empty(self):
        result = super_algos.find_possible_strings([], 3)
        self.assertEqual([], result)

    def test_step3_find_strings_not_chars(self):
        result = super_algos.find_possible_strings([1,2,3,4], 3)
        self.assertEqual([], result)

    def test_unittest_exist(self):
        import test_algos
        self.assertTrue('test_algos' in sys.modules, "test_algos module should be found")

    def test_unittest_succeeds(self):
        import test_algos
        test_result = run_unittests("test_algos")
        self.assertTrue(test_result.wasSuccessful(), "unit tests should succeed")


if __name__ == '__main__':
    unittest.main()
