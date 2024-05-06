# https://leetcode.com/problems/two-sum/description/

import unittest


class Solution:
    def twoSum(self, nums, target):
        diffs = {}

        for i in range(len(nums)):
            if nums[i] in diffs:
                return [diffs[nums[i]], i]

            diffs[target - nums[i]] = i

        return [-1, -1]


param_list = [
    [[0, 1], [2, 7, 11, 15], 9],
    [[1, 2], [3, 2, 4], 6],
    [[0, 1], [3, 3], 6],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, people, limit in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().twoSum(people, limit))


if __name__ == "__main__":
    unittest.main()
