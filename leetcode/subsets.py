# https://leetcode.com/problems/subsets


import unittest


class Solution(object):
    def subsets(self, nums, parent_set = [], depth=0):
        current_sets = []

        for i in range(len(nums)):
            current_sets += [parent_set + [nums[i]]]

        for i in range(len(current_sets) - 1):
            current_sets += self.subsets(nums[i + 1:], current_sets[i], depth + 1)

        return current_sets if depth else [[]] + current_sets


param_list = [
    [[[]], []],
    [[[], [1]], [1]],
    [[[], [1], [2], [1, 2]], [1, 2]],
    [[[], [1], [2], [3], [1, 2], [1, 3], [1, 2, 3], [2, 3]], [1, 2, 3]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, nums in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    Solution().subsets(nums),
                )


if __name__ == "__main__":
    unittest.main()
