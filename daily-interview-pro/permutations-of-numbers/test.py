import unittest
from solution import permute


class Test(unittest.TestCase):

    def test_permute(self):
        self.assertEqual([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], permute([1, 2, 3]))
        self.assertEqual([[1, 2, 3, 4],
                          [1, 2, 4, 3],
                          [1, 3, 2, 4],
                          [1, 3, 4, 2],
                          [1, 4, 2, 3],
                          [1, 4, 3, 2],
                          [2, 1, 3, 4],
                          [2, 1, 4, 3],
                          [2, 3, 1, 4],
                          [2, 3, 4, 1],
                          [2, 4, 1, 3],
                          [2, 4, 3, 1],
                          [3, 1, 2, 4],
                          [3, 1, 4, 2],
                          [3, 2, 1, 4],
                          [3, 2, 4, 1],
                          [3, 4, 1, 2],
                          [3, 4, 2, 1],
                          [4, 1, 2, 3],
                          [4, 1, 3, 2],
                          [4, 2, 1, 3],
                          [4, 2, 3, 1],
                          [4, 3, 1, 2],
                          [4, 3, 2, 1]],
                         permute([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
