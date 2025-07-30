# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch

import unittest


class Solution:
    def removeDuplicates(self, s):
        i = 0

        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2 :]
                i -= 1
            else:
                i += 1

        return s


param_list = [
    ["ca", "abbaca"],
    ["ay", "azxxzy"],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, s in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().removeDuplicates(s))


if __name__ == "__main__":
    unittest.main()
