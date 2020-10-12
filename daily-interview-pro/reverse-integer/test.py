import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(321, Solution().reverse(123))
        self.assertEqual(-321, Solution().reverse(-123))
        self.assertEqual(0, Solution().reverse(2**31))


if __name__ == '__main__':
    unittest.main()
