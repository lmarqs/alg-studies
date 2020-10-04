import unittest
from solution import products1, products2


class Test(unittest.TestCase):

    def test_products(self):
        self.assertEqual([120, 60, 40, 30, 24], products1([1, 2, 3, 4, 5]))
        self.assertEqual([120, 60, 40, 30, 24], products2([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
