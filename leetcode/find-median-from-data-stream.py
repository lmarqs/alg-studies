# https://leetcode.com/problems/find-median-from-data-stream

import unittest
import heapq


class MedianFinder:
    def __init__(self):
        self.top_half = []
        self.bottom_half = []

    def addNum(self, num: int) -> None:
        if self.bottom_half and -self.bottom_half[0] < num:
            heapq.heappush(self.top_half, num)
        else:
            heapq.heappush(self.bottom_half, -num)

        if len(self.bottom_half) > len(self.top_half):
            median = heapq.heappop(self.bottom_half)
            heapq.heappush(self.top_half, -median)

        if len(self.top_half) > len(self.bottom_half):
            median = heapq.heappop(self.top_half)
            heapq.heappush(self.bottom_half, -median)

    def findMedian(self) -> float:
        if len(self.top_half) > len(self.bottom_half):
            return self.top_half[0]

        if len(self.bottom_half) > len(self.top_half):
            return -self.bottom_half[0]

        return (self.top_half[0] - self.bottom_half[0]) / 2


param_list = [
    [3, [2, 3, 4]],
    [2.5, [2, 3]],
    [3, [1, 2, 3, 4, 5]],
    [3.5, [1, 2, 3, 4, 5, 6]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, arr in param_list:
            with self.subTest():
                mf = MedianFinder()

                for num in arr:
                    mf.addNum(num)

                self.assertEqual(expected, mf.findMedian())


if __name__ == "__main__":
    unittest.main()
