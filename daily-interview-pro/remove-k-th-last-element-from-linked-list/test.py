import unittest
from solution import Node, remove_kth_from_linked_list


def buildLinkedList():
    return Node(1, Node(2, Node(3, Node(4, Node(5)))))


class Test(unittest.TestCase):

    def test_remove_kth_from_linked_list(self):
        self.assertEqual(None, remove_kth_from_linked_list(Node(1), 1))

        self.assertEqual([2, 3, 4, 5], remove_kth_from_linked_list(buildLinkedList(), 5).toList())

        self.assertEqual([1, 2, 4, 5], remove_kth_from_linked_list(buildLinkedList(), 3).toList())

        self.assertEqual([1, 2, 3, 4], remove_kth_from_linked_list(buildLinkedList(), 1).toList())


if __name__ == '__main__':
    unittest.main()
