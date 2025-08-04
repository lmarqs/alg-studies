# https://leetcode.com/problems/sort-colors

import unittest


class Solution:
    def sortColors(self, nums):
        zeroes = 0
        ones = 0
        twos = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
                continue

            if nums[i] == 1:
                ones += 1
                continue

            if nums[i] == 2:
                twos += 1
                continue

        for i in range(len(nums)):
            if zeroes:
                nums[i] = 0
                zeroes -= 1
                continue

            if ones:
                nums[i] = 1
                ones -= 1
                continue

            if twos:
                nums[i] = 2
                twos -= 1
                continue


param_list = [
    [[0, 0, 1, 1, 2, 2], [2, 0, 2, 1, 1, 0]],
    [[0, 1, 2], [2, 0, 1]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, nums in param_list:
            with self.subTest():
                Solution().sortColors(nums)
                self.assertEqual(expected, nums)


if __name__ == "__main__":
    unittest.main()
