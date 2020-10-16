import heapq


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    tail = head = Node(-1)
    h = [(l.val, l) for l in lists]
    heapq.heapify(h)
    while h:
        _, n = heapq.heappop(h)
        head.next = Node(n.val)
        head = head.next
        if n.next:
            heapq.heappush(h, (n.next.val, n.next))

    return tail.next
