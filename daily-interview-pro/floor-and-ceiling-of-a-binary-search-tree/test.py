import unittest
from solution import Node, findCeilingFloor


root = Node(8)

root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)


class Test(unittest.TestCase):
    def test_findCeilingFloor_withEmptyTree(self):
        self.assertEqual([None, None], findCeilingFloor(None, 0))

    def test_findCeilingFloor(self):
        self.assertEqual(findCeilingFloor(root, 1), [None, 2])
        self.assertEqual(findCeilingFloor(root, 2), [2, 2])
        self.assertEqual(findCeilingFloor(root, 3), [2, 4])
        self.assertEqual(findCeilingFloor(root, 4), [4, 4])
        self.assertEqual(findCeilingFloor(root, 5), [4, 6])
        self.assertEqual(findCeilingFloor(root, 6), [6, 6])
        self.assertEqual(findCeilingFloor(root, 7), [6, 8])
        self.assertEqual(findCeilingFloor(root, 8), [8, 8])
        self.assertEqual(findCeilingFloor(root, 9), [8, 10])
        self.assertEqual(findCeilingFloor(root, 10), [10, 10])
        self.assertEqual(findCeilingFloor(root, 11), [10, 12])
        self.assertEqual(findCeilingFloor(root, 12), [12, 12])
        self.assertEqual(findCeilingFloor(root, 13), [12, 14])
        self.assertEqual(findCeilingFloor(root, 14), [14, 14])
        self.assertEqual(findCeilingFloor(root, 15), [14, None])


if __name__ == "__main__":
    unittest.main()
