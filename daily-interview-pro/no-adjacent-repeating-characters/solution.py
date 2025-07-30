import collections
import heapq


def rearrangeString(s):
    occurrences = collections.defaultdict(int)

    for c in s:
        occurrences[c] += 1

    heap = [(-count, char) for char, count in occurrences.items()]
    heapq.heapify(heap)

    ans = ""
    prev_count, prev_char = 0, ""

    while heap:
        count, char = heapq.heappop(heap)
        ans += char

        if prev_count < -1:
            heapq.heappush(heap, (prev_count + 1, prev_char))

        prev_count, prev_char = count, char
    return ans
