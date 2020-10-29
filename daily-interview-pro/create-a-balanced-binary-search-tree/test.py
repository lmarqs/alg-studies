import unittest
from solution import createBalancedBST


class Test(unittest.TestCase):
    def test_createBalancedBST(self):
        self.assertEquals('4261357', createBalancedBST([1, 2, 3, 4, 5, 6, 7]).__str__())
        #   4
        #  / \
        # 2   6
        #/ \ / \
        #1 3 5 7


if __name__ == '__main__':
    unittest.main()
