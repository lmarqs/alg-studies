import unittest
from solution import Node, count_unival_subtrees


class Test(unittest.TestCase):
    def test_count_unival_subtrees(self):
        a = Node(0, Node(1, Node(1), Node(1)), Node(0, Node(1), Node(0)))
        self.assertEqual(5, count_unival_subtrees(a))


if __name__ == "__main__":
    unittest.main()
