class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        ans = 0
        head = 0

        for i in range(len(s)):
            c = s[i]

            if c in last_seen:
              while s[head] != c:
                del last_seen[s[head]]
                head += 1
              head += 1

            last_seen[c] = i
            ans = max(ans, i - head + 1)

        return ans
