# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch

import unittest


class Solution:
    def countStudents(self, students, sandwiches):
        hasnt_eaten = 0

        while hasnt_eaten < len(students):
            if students[-1] == sandwiches[0]:
                students = students[:-1]
                sandwiches = sandwiches[1:]
                hasnt_eaten = 0
            else:
                students = students[-1:] + students[0:-1]
                hasnt_eaten += 1

        return len(students)


param_list = [
    [0, [1, 1, 0, 0], [0, 1, 0, 1]],
    [3, [1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, students, sandwiches in param_list:
            with self.subTest():
                self.assertEqual(
                    expected, Solution().countStudents(students, sandwiches)
                )


if __name__ == "__main__":
    unittest.main()
