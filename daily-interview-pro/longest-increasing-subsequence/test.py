import unittest
from solution import longest_increasing_subsequence


class Test(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        self.assertEqual(0, longest_increasing_subsequence([]))
        self.assertEqual(1, longest_increasing_subsequence([1]))
        self.assertEqual(2, longest_increasing_subsequence([1, 2]))
        self.assertEqual(2, longest_increasing_subsequence([1, 2, 1]))
        self.assertEqual(3, longest_increasing_subsequence([1, 2, 1, 3]))
        self.assertEqual(4, longest_increasing_subsequence([1, 2, 1, 2, 3, 4, 3]))

        self.assertEqual(len([0, 2, 6, 9, 11, 15]), longest_increasing_subsequence(
            [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))


if __name__ == '__main__':
    unittest.main()
