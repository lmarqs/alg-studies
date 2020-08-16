import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_minSubArrayLen_withEmptyArray(self):
        self.assertEqual(0, Solution().minSubArrayLen([], 0))

    def test_minSubArrayLen_withArrayContainingSingleValue(self):
        self.assertEqual(1, Solution().minSubArrayLen([1], 0))
        self.assertEqual(1, Solution().minSubArrayLen([1], 1))
        self.assertEqual(0, Solution().minSubArrayLen([1], 2))

    def test_minSubArrayLen_withArrayContainingMultipleValues(self):
        self.assertEqual(1, Solution().minSubArrayLen([1, 2, 3], 1))
        self.assertEqual(1, Solution().minSubArrayLen([1, 2, 3], 2))
        self.assertEqual(1, Solution().minSubArrayLen([1, 2, 3], 3))
        self.assertEqual(2, Solution().minSubArrayLen([1, 2, 3], 4))
        self.assertEqual(2, Solution().minSubArrayLen([1, 2, 3], 5))
        self.assertEqual(3, Solution().minSubArrayLen([1, 2, 3], 6))
        self.assertEqual(0, Solution().minSubArrayLen([1, 2, 3], 7))


if __name__ == '__main__':
    unittest.main()
