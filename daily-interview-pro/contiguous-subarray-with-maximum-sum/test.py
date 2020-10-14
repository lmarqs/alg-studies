import unittest
from solution import max_subarray_sum


class Test(unittest.TestCase):

    def test_max_subarray_sum_with_empty_array(self):
        self.assertEqual(0, max_subarray_sum([]))

    def test_max_subarray_sum_with_only_positive_numbers(self):
        self.assertEqual(1, max_subarray_sum([1]))
        self.assertEqual(6, max_subarray_sum([1, 2, 3]))

    def test_max_subarray_sum_with_only_negative_numbers(self):
        self.assertEqual(-1, max_subarray_sum([-1, -2, -3]))
        self.assertEqual(-1, max_subarray_sum([-3, -2, -1]))

    def test_max_subarray_sum(self):
        self.assertEqual(100, max_subarray_sum([100, -100]))
        self.assertEqual(100, max_subarray_sum([-100, 100]))
        self.assertEqual(7, max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
        self.assertEqual(137, max_subarray_sum([34, -50, 42, 14, -5, 86]))


if __name__ == '__main__':
    unittest.main()
