import unittest
from solution import sortNums


class Test(unittest.TestCase):

    def test_sortNums(self):
        self.assertEqual([1, 1, 2, 2, 3, 3, 3], sortNums([3, 3, 2, 1, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
