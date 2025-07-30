import unittest
from solution import Node, merge


class Test(unittest.TestCase):
    def test_merge(self):
        a = Node(1, Node(3, Node(5)))
        b = Node(2, Node(4, Node(6)))
        self.assertEqual("123456", merge([a, b]).__str__())


if __name__ == "__main__":
    unittest.main()
