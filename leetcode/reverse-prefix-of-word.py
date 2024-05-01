# https://leetcode.com/problems/reverse-prefix-of-word/description/

import unittest

class Solution:
  def reversePrefix(self, word: str, ch: str) -> str:
    chPos = -1
    for i in range(len(word)):
      if word[i] == ch:
        chPos = i
        break

    if chPos == -1:
      return word

    word = list(word)

    for i in range(int(chPos / 2) + 1):
      word[i], word[chPos - i] = word[chPos - i], word[i]

    return "".join(word)

param_list = [
  ["dcbaefd", "abcdefd", "d"],
  ["zxyxxe", "xyxzxe", "z"],
  ["abcd", "abcd", "z"],
]

class Test(unittest.TestCase):
  def test_reversePrefix(self):
    for expected, word, ch in param_list:
      with self.subTest():
        self.assertEqual(expected, Solution().reversePrefix(word, ch))

if __name__ == '__main__':
    unittest.main()
