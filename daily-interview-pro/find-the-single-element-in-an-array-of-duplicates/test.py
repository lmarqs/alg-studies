import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_findSingle(self):
        self.assertEquals(3, Solution().findSingle([1, 1, 3, 4, 4, 5, 6, 5, 6]))


if __name__ == "__main__":
    unittest.main()
