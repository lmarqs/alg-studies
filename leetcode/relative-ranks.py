# https://leetcode.com/problems/relative-ranks/description/

import unittest


class Solution:
    def findRelativeRanks(self, score):
        positions = {}

        for i in range(len(score)):
            positions[str(score[i])] = i

        score = sorted(score, reverse=True)

        ranking = [""] * len(score)

        special_rank = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }

        for i in range(len(score)):
            rank = str(i + 1)
            ranking[positions[str(score[i])]] = special_rank[rank] if rank in special_rank else rank

        return ranking


param_list = [
    [["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"], [5, 4, 3, 2, 1]],
    [["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"], [10, 3, 8, 9, 4]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, score in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().findRelativeRanks(score))


if __name__ == "__main__":
    unittest.main()
