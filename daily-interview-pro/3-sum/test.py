import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_binarySearch(self):
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 0), -1)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 1), 0)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 3), 2)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 4), 3)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 6), 5)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 7), -1)

        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5], 0, 4, 0), -1)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5], 0, 4, 1), 0)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5], 0, 4, 3), 2)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5], 0, 4, 5), 4)
        self.assertEqual(Solution().binarySearch([1, 2, 3, 4, 5], 0, 4, 6), -1)

    def test_threeSum(self):
        self.assertEqual(
            [[-3, -1, 4], [-3, 1, 2], [-1, -1, 2], [-1, 0, 1]],
            Solution().threeSum([0, 4, -1, 2, -3, 1]),
        )
        self.assertEqual([[-2, 1, 1]], Solution().threeSum([1, -2, 1, 0, 5]))


if __name__ == "__main__":
    unittest.main()
