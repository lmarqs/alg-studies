import unittest
from solution import Node, intersection


class Test(unittest.TestCase):

    def test_intersection(self):
        a = Node(1)
        a.next = Node(2)
        a.next.next = Node(3)
        a.next.next.next = Node(4)

        b = Node(6)
        b.next = a.next.next

        self.assertEqual([3, 4], intersection(a, b).toList())


if __name__ == "__main__":
    unittest.main()
