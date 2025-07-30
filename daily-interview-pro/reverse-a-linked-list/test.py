import unittest
from solution import ListNode


class Test(unittest.TestCase):

    def test_reverseIteratively(self):
        testHead = ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0)))))
        reverse = testHead.reverseIteratively()
        self.assertEqual("0 1 2 3 4 ", reverse.toString())

    def test_reverseRecursively(self):
        testHead = ListNode(4, ListNode(3, ListNode(2, ListNode(1, ListNode(0)))))
        reverse = testHead.reverseRecursively()
        self.assertEqual("0 1 2 3 4 ", reverse.toString())


if __name__ == "__main__":
    unittest.main()
