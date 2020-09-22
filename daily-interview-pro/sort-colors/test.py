import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_sortColors(self):
        colors = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
        expected = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]

        self.assertEqual(expected, Solution().sortColors1(colors))
        self.assertEqual(expected, Solution().sortColors2(colors))


if __name__ == '__main__':
    unittest.main()
