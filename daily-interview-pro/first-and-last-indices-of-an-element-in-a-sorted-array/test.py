import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_getRange_withEmpty(self):
        self.assertEqual([-1, -1], Solution().getRange([], 0))

    def test_getRange_withSingleOcurrence(self):
        self.assertEqual([0, 0], Solution().getRange([0], 0))

    def test_getRange_withNoOcurrence1(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 6, 10], 9))

    def test_getRange_withNoOcurrence2(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 6, 10], 11))

    def test_getRange_withNoOcurrence3(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 7], 6))

    def test_getRange_withNoOcurrence4(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 6], 7))

    def test_getRange_withNoOcurrence5(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 7], -1))

    def test_getRange_withNoOcurrence6(self):
        self.assertEqual([-1, -1], Solution().getRange([1, 2, 3, 4, 5, 6, 7], -1))

    def test_getRange_withMultipleOcurrences1(self):
        self.assertEqual([0, 3], Solution().getRange([0, 0, 0, 0], 0))

    def test_getRange_withMultipleOcurrences2(self):
        self.assertEqual([1, 4], Solution().getRange([-1, 0, 0, 0, 0, 1], 0))

    def test_getRange_withMultipleOcurrences3(self):
        self.assertEqual([1, 4], Solution().getRange([1, 2, 2, 2, 2, 3, 4, 5, 6], 2))

    def test_getRange_withMultipleOcurrences4(self):
        self.assertEqual(
            [6, 8], Solution().getRange([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9)
        )

    def test_getRange_withMultipleOcurrences5(self):
        self.assertEqual([1, 2], Solution().getRange([100, 150, 150, 153], 150))

    def test_getRange_withMultipleOcurrences6(self):
        self.assertEqual([5, 5], Solution().getRange([1, 2, 2, 2, 2, 3, 4, 5, 6], 3))

    def test_getRange_withMultipleOcurrences7(self):
        self.assertEqual([1, 2], Solution().getRange([1, 2, 2, 3, 3, 3, 3], 2))

    def test_getRange_withMultipleOcurrences8(self):
        self.assertEqual([3, 6], Solution().getRange([1, 2, 2, 3, 3, 3, 3], 3))


if __name__ == "__main__":
    unittest.main()
