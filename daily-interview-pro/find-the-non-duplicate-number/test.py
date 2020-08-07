import unittest
from solution import singleNumber1, singleNumber2

param_list = [
    [1, [4, 3, 2, 4, 1, 3, 2]],
    [4, [4, 3, 2, 1, 1, 3, 2]],
    [2, [4, 3, 2, 4, 1, 3, 1]],
]
class Test(unittest.TestCase):

    def test_singleNumber(self):
        for expected_value, arr in param_list:
            with self.subTest():
                self.assertEqual(expected_value, singleNumber1(arr))
                self.assertEqual(expected_value, singleNumber2(arr))


if __name__ == '__main__':
    unittest.main()
