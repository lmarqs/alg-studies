import unittest
from solution import buy_and_sell


class Test(unittest.TestCase):

    def test_buy_and_sell(self):
        self.assertEquals(0, buy_and_sell([]))
        self.assertEquals(0, buy_and_sell([1]))
        self.assertEquals(1, buy_and_sell([1, 2]))
        self.assertEquals(5, buy_and_sell([9, 11, 8, 5, 7, 10]))


if __name__ == "__main__":
    unittest.main()
