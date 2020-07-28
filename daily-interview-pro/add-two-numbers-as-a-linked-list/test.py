import unittest
from solution import Solution, ListNode


class Test(unittest.TestCase):

    def test_addTwoNumbers_withSingleDigit_shouldReturnSingleDigitResult(self):
        l1 = ListNode(2)
        l2 = ListNode(5)

        result = Solution().addTwoNumbers(l1, l2)

        self.assertEquals([7], result.toArray())

    def test_addTwoNumbers_withSingleDigit_shouldReturnTwoDigitResult(self):
        l1 = ListNode(9)
        l2 = ListNode(8)

        result = Solution().addTwoNumbers(l1, l2)

        self.assertEquals([7, 1], result.toArray())

    def test_addTwoNumbers_withTwoDigits_shouldReturnTwoDigitResult(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)

        l2 = ListNode(2)
        l2.next = ListNode(4)

        result = Solution().addTwoNumbers(l1, l2)

        self.assertEquals([3, 6], result.toArray())

    def test_addTwoNumbers_withTwoDigits_shouldReturnTreeDigitResult(self):
        l1 = ListNode(9)
        l1.next = ListNode(8)

        l2 = ListNode(7)
        l2.next = ListNode(6)

        result = Solution().addTwoNumbers(l1, l2)

        self.assertEquals([6, 5, 1], result.toArray())

    def test_addTwoNumbers_withTreeDigits_shouldReturnTreeDigitResult(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = Solution().addTwoNumbers(l1, l2)

        self.assertEquals([7, 0, 8], result.toArray())


if __name__ == '__main__':
    unittest.main()
