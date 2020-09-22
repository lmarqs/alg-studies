class Solution:
    def sortColors1(self, nums):
        head = 0
        tail = len(nums) - 1

        sortedNums = [1] * len(nums)

        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                sortedNums[head] = 0
                head += 1
            elif n == 2:
                sortedNums[tail] = 2
                tail -= 1

        return sortedNums

    def sortColors2(self, nums):
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            n = nums[curr]
            if n == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif n == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1
        return nums
