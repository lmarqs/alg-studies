import unittest
from solution import two_sum


class Test(unittest.TestCase):

    def test_two_sum1(self):
        self.assertEqual(True, two_sum([4, 7, 1, -3, 2], 5))

    def test_two_sum2(self):
        self.assertEqual(False, two_sum([4, 7], 5))

    def test_two_sum3(self):
        self.assertEqual(True, two_sum([4, 7], 11))


if __name__ == "__main__":
    unittest.main()
