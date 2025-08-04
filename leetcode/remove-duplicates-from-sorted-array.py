# https://leetcode.com/problems/remove-duplicates-from-sorted-array

import unittest

class Solution:
    def removeDuplicates(self, nums):
        read = 0
        write = 0

        while read < len(nums):
            if nums[write] == nums[read]:
                read += 1
                continue

            write += 1
            nums[write] = nums[read]

        return write + 1

param_list = [
    [[1,2], [1,1,2]],
    [[0,1,2,3,4], [0,0,1,1,1,2,2,3,3,4]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, nums in param_list:
            with self.subTest():
                k = Solution().removeDuplicates(nums)

                self.assertEqual(len(expected), k)

                for i in range(k):
                    self.assertEqual(expected[i], nums[i])



if __name__ == "__main__":
    unittest.main()
