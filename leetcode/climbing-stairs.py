# https://leetcode.com/problems/climbing-stairs
import unittest

class Solution(object):
    def climbStairs(self, n):
        n += 1
        steps = [1] * n

        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[-1]

param_list = [
    [1, 1],
    [2, 2],
    [3, 3],
    [6765, 19],
    [832040, 29],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, n in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().climbStairs(n))


if __name__ == "__main__":
    unittest.main()
