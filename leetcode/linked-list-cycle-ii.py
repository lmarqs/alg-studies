# https://leetcode.com/problems/reverse-linked-list

import unittest


class ListNode:
    def __init__(self, val=0, next=None, pos=0):
        self.val = val
        self.next = next
        self.pos = pos


def toLinkedList(values):
    head = None

    for pos in range(len(values) - 1, -1, -1):
        head = ListNode(values[pos], head, pos)

    return head


def toList(head):
    values = []

    while head != None:
        values += [head.val]
        head = head.next

    return values


class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


param_list = [
    [1, [3,2,0,-4]],
    [1, [1,2]],
    [-1, [1]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, case in param_list:
            with self.subTest():
                head = toLinkedList(case)

                if expected >= 0:
                    tail = head
                    cycle = head

                    while tail.next:
                        tail = tail.next
                        cycle = cycle if tail.pos != expected else tail

                    tail.next = cycle

                result = Solution().detectCycle(head)

                print(expected, case)

                self.assertEqual(expected, result.pos if result else -1)


if __name__ == "__main__":
    unittest.main()
