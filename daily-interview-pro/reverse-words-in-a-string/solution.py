class Solution:
    def reverseWords(self, s):
        ans = ''
        tail = head = 0

        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                ans += s[tail:head+1][::-1]
                ans += c
                tail = i + 1
            else:
                head = i

        ans += s[tail:head+1][::-1]
        return ans
