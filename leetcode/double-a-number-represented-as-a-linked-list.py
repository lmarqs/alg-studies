# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toLinkedList(values):
    head = None

    for i in range(len(values) - 1, -1, -1):
        head = ListNode(values[i], head)

    return head

def toList(head):
    values = []

    while head != None:
        values += [head.val]
        head = head.next

    return values

class Solution(object):
    def doubleIt(self, head):
        double = 0

        while head != None:
            double *= 10
            double += head.val
            head = head.next

        double = double * 2

        head = None if double else ListNode()

        while double:
            head = ListNode(double % 10, head)
            double //= 10

        return head


param_list = [
    [[3,7,8], [1,8,9]],
    [[1,9,9,8], [9,9,9]],
    [[1,0], [5]],
    [[0], [0]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, values in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    toList(Solution().doubleIt(toLinkedList(values))),
                )


if __name__ == "__main__":
    unittest.main()
