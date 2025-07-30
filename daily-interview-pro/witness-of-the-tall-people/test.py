import unittest
from solution import witnesses


class Test(unittest.TestCase):

    def test_witnesses(self):
        self.assertEqual(3, witnesses([3, 6, 3, 4, 1]))


if __name__ == "__main__":
    unittest.main()
