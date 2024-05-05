# https://leetcode.com/problems/compare-version-numbers/

import unittest


class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")

        for i in range(max(len(version1), len(version2))):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0

            if v1 > v2:
                return 1

            if v1 < v2:
                return -1

        return 0


param_list = [
    [0, "1.01", "1.001"],
    [1, "1.0.1", "1.0.0"],
    [1, "1.0001.0", "1.0.0"],
    [-1, "1.0.0", "1.0.1"],
    [0, "1.0", "1.0.0"],
    [-1, "0.1", "1.1"],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, version1, version2 in param_list:
            with self.subTest():
                self.assertEqual(
                    expected, Solution().compareVersion(version1, version2)
                )


if __name__ == "__main__":
    unittest.main()
