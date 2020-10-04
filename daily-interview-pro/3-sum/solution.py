class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        results = []

        index_to_check = 0

        while index_to_check < len(nums) and nums[index_to_check] < 0:
            head = index_to_check
            tail = len(nums) - 1

            while nums[head] <= 0 and nums[tail] >= 0:
                idx = self.binarySearch(nums, head, tail, -(nums[head] + nums[tail]))

                if idx != -1:
                    results += [[nums[head], nums[idx], nums[tail]]]

                tail = self.nextIndexWithDifferentNumber(nums, tail, -1)

            index_to_check = self.nextIndexWithDifferentNumber(nums, index_to_check, 1)
        return results

    def nextIndexWithDifferentNumber(self, nums, idx, step):
        n = nums[idx]
        while idx > 0 and idx < len(nums) - 1 and nums[idx + step] == n:
            idx += step
        return idx + step

    def binarySearch(self, numbers, lower, upper, target):
        if lower > upper:
            return -1

        middle = (lower + upper) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            return self.binarySearch(numbers, middle + 1, upper, target)
        else:
            return self.binarySearch(numbers, lower, middle - 1, target)
