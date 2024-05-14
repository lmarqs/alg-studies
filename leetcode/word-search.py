# https://leetcode.com/problems/word-search

import unittest


class Solution:
    def __init__(self):
        self.visited = {}

    def backtrack(self, i, j, board, word, depth=0):
        if depth >= len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False

        key = "{},{}".format(i, j)

        if key in self.visited:
            return False

        if word[depth] != board[i][j]:
            return False

        self.visited[key] = True
        found = False

        found = self.backtrack(i - 1, j, board, word, depth + 1) if not found else found
        found = self.backtrack(i + 1, j, board, word, depth + 1) if not found else found
        found = self.backtrack(i, j - 1, board, word, depth + 1) if not found else found
        found = self.backtrack(i, j + 1, board, word, depth + 1) if not found else found

        self.visited.pop(key)

        return found

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtrack(i, j, board, word):
                    return True

        return False


param_list = [
    [True, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"],
    [True, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"],
    [False, [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"],
    [True, [["a"]], "a"],
    [True, [["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"]
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, board, word in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().exist(board, word))


if __name__ == "__main__":
    unittest.main()
