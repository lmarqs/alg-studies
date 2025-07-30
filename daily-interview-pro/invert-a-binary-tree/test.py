import unittest
from solution import Node, invert


root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")


class Test(unittest.TestCase):
    def test_invert(self):
        self.assertEquals("abdecf", root.preorder())
        invert(root)
        self.assertEquals("acfbed", root.preorder())


if __name__ == "__main__":
    unittest.main()
