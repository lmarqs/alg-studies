# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

import unittest

class Solution:
    def subsetXORSum(self, nums, xor=0):
        s = 0
        xors = []

        for i in range(len(nums)):
            xors += [xor ^ nums[i]]
            s += xors[-1]

        for i in range(len(xors) - 1):
            s += self.subsetXORSum(nums[i + 1:], xors[i])

        return s


param_list = [
    [6, [1, 3]],
    [28, [5, 1, 6]],
    [480, [3, 4, 5, 6, 7, 8]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, nums in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    Solution().subsetXORSum(nums),
                )


if __name__ == "__main__":
    unittest.main()
