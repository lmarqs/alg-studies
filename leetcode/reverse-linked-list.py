# https://leetcode.com/problems/reverse-linked-list

import unittest


class ListNode:
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


class Solution:
    def reverseList(self, head):
        prev = None
        cur = head

        while cur:
            next = cur.next

            cur.next = prev

            prev = cur
            cur = next

        return prev


param_list = [
    [[], []],
    [[1], [1]],
    [[1, 2, 3], [3, 2, 1]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, case in param_list:
            with self.subTest():
                self.assertEqual(
                    expected, toList(Solution().reverseList(toLinkedList(case)))
                )


if __name__ == "__main__":
    unittest.main()
