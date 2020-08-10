import unittest
from solution import findPythagoreanTriplets

param_list = [
    [False, []],
    [False, [3]],
    [False, [3, 4]],
    [False, [3, 4, 6]],
    [True, [3, 4, 5]],
    [True, [3, 5, 12, 5, 13]]
]


class Test(unittest.TestCase):

    def test_findPythagoreanTriplets(self):
        for expected_value, arr in param_list:
            with self.subTest():
                self.assertEqual(expected_value, findPythagoreanTriplets(arr))


if __name__ == '__main__':
    unittest.main()
