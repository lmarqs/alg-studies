import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual([9, 4], Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))


if __name__ == '__main__':
    unittest.main()
