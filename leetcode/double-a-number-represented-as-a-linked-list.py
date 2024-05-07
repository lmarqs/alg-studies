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
        double = ""

        while head != None:
            double += str(head.val)
            head = head.next

        double = str(int(double) * 2)

        return toLinkedList([int(double[i]) for i in range(len(double))])


param_list = [
    [[3,7,8], [1,8,9]],
    [[1,9,9,8], [9,9,9]],
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
