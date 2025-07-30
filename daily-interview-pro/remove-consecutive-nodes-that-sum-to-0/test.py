import unittest
from solution import Node, removeConsecutiveSumTo0


class Test(unittest.TestCase):

    def test_removeConsecutiveSumTo0(self):
        node = Node(
            0,
            Node(
                10,
                Node(
                    0,
                    Node(
                        -10,
                        Node(
                            10, Node(5, Node(-3, Node(-3, Node(1, Node(4, Node(-4))))))
                        ),
                    ),
                ),
            ),
        )
        self.assertEqual([10], removeConsecutiveSumTo0(node).toList())


if __name__ == "__main__":
    unittest.main()
