import unittest
from solution import Solution


class Test(unittest.TestCase):

    def test_numIslands(self):
        grid = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0]]

        self.assertEqual(3, Solution().numIslands(grid))


if __name__ == "__main__":
    unittest.main()
