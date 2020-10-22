# Sorting - time: O(n log n), space: O(1) to O(n)


def findKthLargestSorting(arr, k):
    return sorted(arr)[-k]

# Max-heap - time: O(n log k), space: O(k)


def findKthLargestMaxHeap(arr, k):
    import heapq

    heap = []
    heapq.heapify(heap)

    for n in arr:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# QuickSelect - time: O(n) to O(n2), space: O(log n) to O(n)


def findKthLargestQuickSelect(arr, k):
    def sort(start, end):
        if start >= end:
            return

        i = middle = start

        while i <= end:
            if arr[start] > arr[i]:
                middle += 1
                arr[middle], arr[i] = arr[i], arr[middle]
            i += 1

        arr[middle], arr[start] = arr[start], arr[middle]

        if len(arr) - k < middle - 1:
            sort(start, middle - 1)
        else:
            sort(middle + 1, end)

    sort(0, len(arr) - 1)

    return arr[-k]
