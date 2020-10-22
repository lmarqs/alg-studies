import unittest
from solution import findKthLargestSorting, findKthLargestMaxHeap, findKthLargestQuickSelect


class Test(unittest.TestCase):
    def test_findKthLargestSorting(self):

        self.assertEquals(8, findKthLargestSorting([3, 5, 2, 4, 6, 8], 1))
        self.assertEquals(6, findKthLargestSorting([3, 5, 2, 4, 6, 8], 2))
        self.assertEquals(5, findKthLargestSorting([3, 5, 2, 4, 6, 8], 3))
        self.assertEquals(4, findKthLargestSorting([3, 5, 2, 4, 6, 8], 4))
        self.assertEquals(3, findKthLargestSorting([3, 5, 2, 4, 6, 8], 5))
        self.assertEquals(2, findKthLargestSorting([3, 5, 2, 4, 6, 8], 6))

    def test_findKthLargestMaxHeap(self):

        self.assertEquals(8, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 1))
        self.assertEquals(6, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 2))
        self.assertEquals(5, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 3))
        self.assertEquals(4, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 4))
        self.assertEquals(3, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 5))
        self.assertEquals(2, findKthLargestMaxHeap([3, 5, 2, 4, 6, 8], 6))

    def test_findKthLargestQuickSelect(self):

        self.assertEquals(1, findKthLargestQuickSelect([1], 1))
        self.assertEquals(2, findKthLargestQuickSelect([1, 2], 1))
        self.assertEquals(1, findKthLargestQuickSelect([1, 2], 2))
        self.assertEquals(3, findKthLargestQuickSelect([1, 2, 3], 1))
        self.assertEquals(2, findKthLargestQuickSelect([1, 2, 3], 2))
        self.assertEquals(1, findKthLargestQuickSelect([1, 2, 3], 3))

        self.assertEquals(8, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 1))
        self.assertEquals(6, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 2))
        self.assertEquals(5, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 3))
        self.assertEquals(4, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 4))
        self.assertEquals(3, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 5))
        self.assertEquals(2, findKthLargestQuickSelect([3, 5, 2, 4, 6, 8], 6))


if __name__ == '__main__':
    unittest.main()
