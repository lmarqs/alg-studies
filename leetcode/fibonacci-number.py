# https://leetcode.com/problems/fibonacci-number/description/

import unittest

class Solution(object):
    def fib(self, n):
        return 0


param_list = [
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, n in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().fib(n))


if __name__ == "__main__":
    unittest.main()
