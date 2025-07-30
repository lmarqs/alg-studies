import unittest
from solution import serialize, deserialize, Node


class Test(unittest.TestCase):

    def test_serialize(self):
        #     1
        #    / \
        #   3   4
        #  / \   \
        # 2   5   7
        tree = Node(1)
        tree.left = Node(3)
        tree.left.left = Node(2)
        tree.left.right = Node(5)
        tree.right = Node(4)
        tree.right.right = Node(7)

        self.assertEqual("1 3 2 # # 5 # # 4 # 7 # #", serialize(tree))

    def test_deserialize(self):
        self.assertEqual("132547", deserialize("1 3 2 # # 5 # # 4 # 7 # #").__str__())


if __name__ == "__main__":
    unittest.main()
