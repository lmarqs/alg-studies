# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

import unittest

class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) < 2:
      return len(s)

    positions = {}
    max_len = 0
    tail = head = 0

    while head < len(s):
      ch = s[head]

      if ch in positions:
        tail = max(tail, positions.pop(ch) + 1)

      positions[ch] = head
      head = max(head, tail) + 1

      max_len = max(head - tail, max_len)

    return max_len

param_list = [
  [3, "abcabcbb"],
  [1, "bbbbb"],
  [3, "pwwkew"],
  [1, " "],
  [2, "abba"],
  [5, "tmmzuxt"]
]

class Test(unittest.TestCase):
  def test_reversePrefix(self):
    for expected, s in param_list:
      with self.subTest():
        self.assertEqual(expected, Solution().lengthOfLongestSubstring(s))

if __name__ == '__main__':
    unittest.main()
