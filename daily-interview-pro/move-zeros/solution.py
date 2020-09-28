class Solution:
    def moveZeros(self, nums):
        gap = 0
        i = 0
        for i in range(len(nums)):
            n = nums[i]

            if n == 0:
                gap += 1
                continue

            nums[i - gap] = n

        for i in range(gap - 1, len(nums)):
            nums[i] = 0

        return nums
