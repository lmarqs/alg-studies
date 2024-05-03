# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

import unittest

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    positions = {}
    max_len = 0
    tail = 0

    for i in range(len(s)):
      ch = s[i]

      if ch in positions:
        tail = positions[ch] + 1

      positions[ch] = i

      max_len = max(i - tail + 1, max_len)

    return max_len

param_list = [
  [3, "abcabcbb"],
  [1, "bbbbb"],
  [3, "pwwkew"],
]

class Test(unittest.TestCase):
  def test_reversePrefix(self):
    for expected, s in param_list:
      with self.subTest():
        self.assertEqual(expected, Solution().lengthOfLongestSubstring(s))

if __name__ == '__main__':
    unittest.main()
