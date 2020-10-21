class Solution(object):
    def findSingle(self, nums):
        a = 0
        for n in nums:
            a ^= n
        return a
