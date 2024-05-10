# https://leetcode.com/problems/add-two-numbers/

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


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        if l1 == None and l2 == None and carry == 0:
            return None

        value = carry
        value += l1.val if l1 else 0
        value += l2.val if l2 else 0

        return ListNode(
            value % 10,
            self.addTwoNumbers(
                l1.next if l1 else None, l2.next if l2 else None, value // 10
            ),
        )


param_list = [
    [[7, 0, 8], [2, 4, 3], [5, 6, 4]],
    [[0], [0], [0]],
    [[8, 9, 9, 9, 0, 0, 0, 1], [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, l1, l2 in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    toList(
                        Solution().addTwoNumbers(
                            toLinkedList(l1),
                            toLinkedList(l2),
                        )
                    ),
                )


if __name__ == "__main__":
    unittest.main()
