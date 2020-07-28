class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def toArray(self):
        node = self
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        return arr


class Solution:
    def addTwoNumbers(self, l1, l2, acc=0):
        val = l1.val + l2.val + acc

        acc = val // 10

        result = ListNode(val % 10)

        if l1.next or l2.next or acc:
            result.next = self.addTwoNumbers(
                l1.next or ListNode(0),
                l2.next or ListNode(0),
                acc
            )

        return result
