# https://leetcode.com/problems/delete-leaves-with-a-given-value

import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def toList(self):
        result = [self.val]
        if self.left:
            result.extend(self.left.toList())
        if self.right:
            result.extend(self.right.toList())
        return result


class Solution(object):
    def removeLeafNodes(self, root, target):

        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root


param_list = [
    [
        [1, None, 3, None, 4],
        TreeNode(
            1, TreeNode(2, TreeNode(2), None), TreeNode(3, TreeNode(2), TreeNode(4))
        ),
        2,
    ],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, root, target in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    Solution().removeLeafNodes(root, target).toList(),
                )


if __name__ == "__main__":
    unittest.main()
