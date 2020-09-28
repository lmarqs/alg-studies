import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_moveZeros(self):
        self.assertEqual([2, 1, 3, 4, 0, 0, 0, 0, 0, 0], Solution().moveZeros([0, 0, 0, 2, 0, 1, 3, 4, 0, 0]))


if __name__ == '__main__':
    unittest.main()
