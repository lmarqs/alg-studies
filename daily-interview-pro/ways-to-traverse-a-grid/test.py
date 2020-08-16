import unittest
from solution import num_ways


class Test(unittest.TestCase):

    def test_num_ways(self):
        self.assertEqual(1, num_ways(1, 1))
        self.assertEqual(1, num_ways(1, 2))
        self.assertEqual(1, num_ways(1, 3))
        self.assertEqual(1, num_ways(1, 4))

        self.assertEqual(1, num_ways(1, 1))
        self.assertEqual(1, num_ways(2, 1))
        self.assertEqual(1, num_ways(3, 1))
        self.assertEqual(1, num_ways(4, 1))

        self.assertEqual(2, num_ways(2, 2))
        self.assertEqual(3, num_ways(2, 3))
        self.assertEqual(4, num_ways(2, 4))

        self.assertEqual(6, num_ways(3, 3))
        self.assertEqual(10, num_ways(4, 3))

        self.assertEqual(6, num_ways(3, 3))
        self.assertEqual(10, num_ways(3, 4))

        self.assertEqual(20, num_ways(4, 4))


if __name__ == '__main__':
    unittest.main()
