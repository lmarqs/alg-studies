import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_pushDominoes(self):
        self.assertEqual('LLL....RR.LL.RL.RRLL.RR', Solution().pushDominoes('..L....R...L.RL.R..L.R.'))


if __name__ == '__main__':
    unittest.main()
