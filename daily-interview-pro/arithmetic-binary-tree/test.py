import unittest
from solution import Node, evaluate


class Test(unittest.TestCase):

    def test_evaluate(self):
        #         *
        #       /   \
        #      +     +
        #    /   \  /  \
        #   -    2 4    5
        #    \
        #     -3

        tree = Node("*")
        tree.left = Node("+")
        tree.left.left = Node("-")
        tree.left.left.right = Node(-3)
        tree.left.right = Node(2)
        tree.right = Node("+")
        tree.right.left = Node(4)
        tree.right.right = Node(5)

        self.assertEqual(45, evaluate(tree))


if __name__ == "__main__":
    unittest.main()
