class Solution:
    def lengthOfLongestSubstring(self, text):
        last_seen = {}
        result = 0
        tail = -1

        for head in range(len(text)):
            char = text[head]

            if char in last_seen:
                tail = max(tail, last_seen[char])

            last_seen[char] = head
            result = max(result, head - tail)

        return result
