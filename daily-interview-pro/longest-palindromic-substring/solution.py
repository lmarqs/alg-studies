class Solution:
    def longestPalindrome(self, text):
        result = ""
        for i in range(1, len(text)):
            result = self.scanFromPalindrome(text, result, i, i)
            result = self.scanFromPalindrome(text, result, i - 1, i)

        return result

    def scanFromPalindrome(self, text, result, tail, head):
        while head < len(text) and tail >= 0 and text[head] == text[tail]:
            if head - tail > len(result):
                result = text[tail : head + 1]

            head += 1
            tail -= 1

        return result
