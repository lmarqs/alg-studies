class Solution:
    def minSubArrayLen(self, nums, s):
        tail = 0
        head = -1
        sum = 0
        ans = len(nums) + 1
        for n in nums:
            head += 1
            sum += n

            while tail < head and sum - nums[tail] >= s:
                sum -= nums[tail]
                tail += 1

            if sum >= s and head - tail < ans:
              ans = head - tail + 1

        return ans if ans <= len(nums) else 0
