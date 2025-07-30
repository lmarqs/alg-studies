import unittest
from solution import distance


class Test(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(2, distance("biting", "sitting"))


if __name__ == "__main__":
    unittest.main()
