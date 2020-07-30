class Solution:
    def lengthOfLongestSubstring(self, text):
        last_seen = {}
        ans = 0
        head = 0

        for tail in range(len(text)):
            char = text[tail]

            if char in last_seen:
              while text[head] != char:
                del last_seen[text[head]]
                head += 1
              head += 1

            last_seen[char] = tail
            ans = max(ans, tail - head + 1)

        return ans
