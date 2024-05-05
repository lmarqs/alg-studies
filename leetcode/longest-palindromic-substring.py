# https://leetcode.com/problems/longest-palindromic-substring/description/

import unittest


class Solution:
    def longestPalindrome(self, s):
        longest = s[0:1]

        for i in range(1, len(s)):
            (start, end) = self.findPalindromeRange(s, i, i)
            if end - start + 1 > len(longest):
                longest = s[start : end + 1]

            (start, end) = self.findPalindromeRange(s, i - 1, i)
            if end - start + 1 > len(longest):
                longest = s[start : end + 1]

        return longest

    def findPalindromeRange(self, s, start, end):
        while start > 0 and end < len(s) - 1 and s[start] == s[end]:
            start -= 1
            end += 1
        return (start, end) if s[start] == s[end] else (start + 1, end - 1)


param_list = [
    ["bab", "babad"],
    ["geeksskeeg", "forgeeksskeegfor"],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, s in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().longestPalindrome(s))


if __name__ == "__main__":
    unittest.main()
