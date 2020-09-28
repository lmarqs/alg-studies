import unittest
from solution import Node, deepest


class Test(unittest.TestCase):

    def test_deepest(self):
        root = Node('a')
        root.left = Node('b')
        root.left.left = Node('d')
        root.right = Node('c')

        n, d = deepest(root)

        self.assertEqual('d', n.val)
        self.assertEqual(3, d)


if __name__ == '__main__':
    unittest.main()
