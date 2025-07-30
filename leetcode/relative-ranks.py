# https://leetcode.com/problems/relative-ranks

import unittest
import heapq


class Solution:
    def findRelativeRanks(self, score):
        heap = []

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))

        special_ranks = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }

        ranking = [""] * len(score)

        for i in range(len(score)):
            (score, idx) = heapq.heappop(heap)
            rank = str(i + 1)
            ranking[idx] = special_ranks[rank] if rank in special_ranks else rank

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
