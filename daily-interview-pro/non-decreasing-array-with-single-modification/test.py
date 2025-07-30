import unittest
from solution import check

param_list = [
    [True, [1, 1, 1]],  # never reseting highest
    [True, [1, 2, 3]],  # never reseting highest
    [False, [4, 6, 3, 3]],  # never reseting highest
    [
        True,
        [4, 6, 4, 4],
    ],  # reseting highest because  ((i) => lst[i] >= lst[2 - i])(2) == True
    [
        True,
        [4, 6, 5, 5],
    ],  # reseting highest because  ((i) => lst[i] >= lst[2 - i])(2) == True
    [True, [2, 1, 2, 2]],  # reseting highest because i == 1
]


class Test(unittest.TestCase):

    def test_check(self):
        for expected_value, arr in param_list:
            with self.subTest():
                self.assertEquals(expected_value, check(arr))


if __name__ == "__main__":
    unittest.main()
