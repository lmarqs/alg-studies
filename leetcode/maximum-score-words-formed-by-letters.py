# https://leetcode.com/problems/maximum-score-words-formed-by-letters


class Solution:
    def convertCharToVectorIndex(self, c):
        return ord(c) - 97

    def createRecurrenceVector(self, word=""):
        recurrence = [0] * 26

        for letter in word:
            recurrence[self.convertCharToVectorIndex(letter)] += 1

        return recurrence

    def addVectors(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def multiplyVectors(self, a, b):
        return [x * y for x, y in zip(a, b)]

    def fits(self, a, b):
        for i in range(len(a)):
            if a[i] > b[i]:
                return False

        return True

    def maxScoreWords(self, words, letters, scores):
        max_allowed_recurrence = self.createRecurrenceVector(letters)

        recurrences = [self.createRecurrenceVector()]
        max_score = 0

        for word in words:
            word_recurrence = self.createRecurrenceVector(word)

            for i in range(len(recurrences)):
                added_recurrence = self.addVectors(word_recurrence, recurrences[i])

                if self.fits(added_recurrence, max_allowed_recurrence):
                    score = sum(self.multiplyVectors(added_recurrence, scores))
                    recurrences += [added_recurrence]
                    max_score = max(max_score, score)

        return max_score


param_list = [
    [
        23,
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [
        27,
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "x"],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
    ],
    [
        0,
        ["leetcode"],
        ["l", "e", "t", "c", "o", "d"],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    ],
    [
        51,
        ["add", "dda", "bb", "ba", "add"],
        [
            "a",
            "a",
            "a",
            "a",
            "b",
            "b",
            "b",
            "b",
            "c",
            "c",
            "c",
            "c",
            "c",
            "d",
            "d",
            "d",
        ],
        [3, 9, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
]

import unittest


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, words, letters, scores in param_list:
            with self.subTest():
                self.assertEqual(
                    expected, Solution().maxScoreWords(words, letters, scores)
                )


if __name__ == "__main__":
    unittest.main()
