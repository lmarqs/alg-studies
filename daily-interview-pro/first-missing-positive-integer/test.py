import unittest
from solution import first_missing_positive


class Test(unittest.TestCase):

    def test_first_missing_positive(self):
        self.assertEqual(2, first_missing_positive([3, 4, -1, 1]))
        self.assertEqual(6, first_missing_positive([3, 4, -1, 1, 5, 2, 8]))
        self.assertEqual(1, first_missing_positive([]))
        self.assertEqual(1, first_missing_positive([0]))


if __name__ == "__main__":
    unittest.main()
