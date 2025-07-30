import unittest
from solution import staircase

param_list = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 5],
    [5, 8],
]


class Test(unittest.TestCase):
    def test_staircase(self):
        for steps, expected_value in param_list:
            with self.subTest():
                self.assertEqual(expected_value, staircase(steps))


if __name__ == "__main__":
    unittest.main()
