import unittest
from solution import maximum_product_of_three


class Test(unittest.TestCase):

    def test_maximum_product_of_three(self):
        self.assertEqual(0, maximum_product_of_three([]))
        self.assertEqual(6, maximum_product_of_three([1, 2, 3]))
        self.assertEqual(120, maximum_product_of_three([1, 2, 3, 4, 5, 6]))
        self.assertEqual(128, maximum_product_of_three([-4, -4, 2, 8]))


if __name__ == '__main__':
    unittest.main()
