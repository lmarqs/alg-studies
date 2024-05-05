# https://leetcode.com/problems/boats-to-save-people/description/

import unittest


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people = sorted(people)

        tail = 0
        head = len(people) - 1
        count = 0

        while head >= tail:
            if people[tail] + people[head] <= limit:
                tail += 1
            head -= 1
            count += 1

        return count


param_list = [
    [1, [1, 2], 3],
    [3, [3, 2, 2, 1], 3],
    [4, [3, 5, 3, 4], 5],
]


class Test(unittest.TestCase):
    def test_reversePrefix(self):
        for expected, people, limit in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().numRescueBoats(people, limit))


if __name__ == "__main__":
    unittest.main()
