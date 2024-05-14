# https://leetcode.com/problems/score-after-flipping-matrix

import unittest


class Solution(object):
    def matrixScore(self, grid):
        for i in range(len(grid)):
            row = grid[i]
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 1 if row[j] == 0 else 0

        for j in range(len(grid[0])):
            zeros_count = 0
            ones_count = 0

            for i in range(len(grid)):
                if grid[i][j] == 0:
                    zeros_count += 1
                else:
                    ones_count += 1

            if zeros_count > ones_count:
                for i in range(len(grid)):
                    grid[i][j] = 1 if grid[i][j] == 0 else 0

        result = 0
        base = 1
        for j in range(len(grid[0]) - 1, -1, -1):
            for i in range(len(grid)):
                result += grid[i][j] * base
            base *= 2
        return result


param_list = [[39, [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]]]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, grid in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().matrixScore(grid))


if __name__ == "__main__":
    unittest.main()
