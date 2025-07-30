# https://leetcode.com/problems/fibonacci-number

import unittest


class Solution(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            return 0

        if n == 1:
            return 1

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.memo[n]


param_list = [
    [0, 0],
    [1, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [6765, 20],
    [832040, 30],
    [9227465, 35],
    [24157817, 37],
    [63245986, 39],
    [280571172992510140037611932413038677189525, 200],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, n in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().fib(n))


if __name__ == "__main__":
    unittest.main()
