import unittest
from solution import largestNum


class Test(unittest.TestCase):

    def test_largestNum(self):
        self.assertEqual("77245217", largestNum([17, 7, 2, 45, 72]))


if __name__ == "__main__":
    unittest.main()
