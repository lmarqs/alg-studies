# https://leetcode.com/problems/incremental-memory-leak

import unittest


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        i = 0

        while True:
            i += 1

            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i

            if memory1 < 0:
                return [i, memory1 + i, memory2]

            if memory2 < 0:
                return [i, memory1, memory2 + i]


param_list = [
    [[3, 1, 0], 2, 2],
    [[6, 0, 4], 8, 11],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, memory1, memory2 in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().memLeak(memory1, memory2))


if __name__ == "__main__":
    unittest.main()
