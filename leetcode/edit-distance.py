# https://leetcode.com/problems/edit-distance/

import unittest


class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1) + 1
        n = len(word2) + 1

        d = [[max(i, j) if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = 1 + min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1])

        return d[-1][-1]

param_list = [
    [0, "b", "b"],
    [1, "banana", "babana"],
    [6, "b", "abbabba"],
    [3, "horse", "ros"],
    [5, "intention", "execution"],
    [2, "biting", "sitting"],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, word1, word2 in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    Solution().minDistance(word1, word2),
                )


if __name__ == "__main__":
    unittest.main()
