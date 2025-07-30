class Solution:
    def reverse(self, x):
        s = 1 if x >= 0 else -1
        r = s * int(str(abs(x))[::-1])
        return 0 if r < -(2**31) or r > (2**31) - 1 else r
