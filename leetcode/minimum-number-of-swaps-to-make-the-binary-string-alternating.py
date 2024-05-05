# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        zeroes = 0
        ones = 0

        for i in range(len(s)):
            if s[i] == "0":
                zeroes += 1
            else:
                ones += 1

        if abs(zeroes - ones) > 1:
            return -1

        c0 = 0
        c1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    c0 += 1
                else:
                    c1 += 1

        return min(c0, c1)


param_list = [
    [-1, "1110"],
    [0, "010"],
    [0, "1010"],
    [1, "000111"],
    [1, "011101000"],
    [1, "100010111"],
    [1, "111000"],
    [3, "11111100000"],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, s in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().minSwaps(s))


if __name__ == "__main__":
    unittest.main()
