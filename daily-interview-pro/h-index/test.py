import unittest
from solution import hIndex1, hIndex2


class Test(unittest.TestCase):

    def test_hIndex1(self):
        self.assertEqual(0, hIndex1([]))
        self.assertEqual(0, hIndex1([0]))
        self.assertEqual(1, hIndex1([5]))
        self.assertEqual(2, hIndex1([5, 6]))
        self.assertEqual(1, hIndex1([1, 1, 1, 1, 1]))
        self.assertEqual(3, hIndex1([3, 5, 0, 1, 3]))
        self.assertEqual(5, hIndex1([3, 5, 0, 1, 3, 5, 5, 5, 5]))

    def test_hIndex2(self):
        self.assertEqual(0, hIndex2([]))
        self.assertEqual(0, hIndex2([0]))
        self.assertEqual(1, hIndex2([1]))
        self.assertEqual(1, hIndex2([5]))
        self.assertEqual(2, hIndex2([5, 6]))
        self.assertEqual(1, hIndex2([1, 1, 1, 1, 1]))
        self.assertEqual(3, hIndex2([3, 5, 0, 1, 3]))
        self.assertEqual(5, hIndex1([3, 5, 0, 1, 3, 5, 5, 5, 5]))


if __name__ == "__main__":
    unittest.main()
