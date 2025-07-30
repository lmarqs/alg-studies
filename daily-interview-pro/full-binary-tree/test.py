import unittest

from solution import fullBinaryTree, Node


class Test(unittest.TestCase):
    def test_romanToInt(self):
        # Given this tree:
        #     1
        #    / \
        #   2   3
        #  /   / \
        # 0   9   4

        # We want a tree like:
        #     1
        #    / \
        #   0   3
        #      / \
        #     9   4

        tree = Node(1)
        tree.left = Node(2)
        tree.right = Node(3)
        tree.right.right = Node(4)
        tree.right.left = Node(9)
        tree.left.left = Node(0)
        self.assertEqual("1\n03\n94", fullBinaryTree(tree).__str__())


if __name__ == "__main__":
    unittest.main()
