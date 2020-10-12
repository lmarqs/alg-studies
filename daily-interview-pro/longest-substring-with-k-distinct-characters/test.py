import unittest
from solution import longest_substring_with_k_distinct_characters


class Test(unittest.TestCase):

    def test_longest_substring_with_k_distinct_characters(self):
        self.assertEqual(3, longest_substring_with_k_distinct_characters('aabbcdbefff', 1))
        self.assertEqual(4, longest_substring_with_k_distinct_characters('aabbcdbefff', 2))
        self.assertEqual(5, longest_substring_with_k_distinct_characters('aabbcdbefff', 3))
        self.assertEqual(7, longest_substring_with_k_distinct_characters('aabbcdbefff', 4))
        self.assertEqual(9, longest_substring_with_k_distinct_characters('aabbcdbefff', 5))
        self.assertEqual(11, longest_substring_with_k_distinct_characters('aabbcdbefff', 11))


if __name__ == '__main__':
    unittest.main()
