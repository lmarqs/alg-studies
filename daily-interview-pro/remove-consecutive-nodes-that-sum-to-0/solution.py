class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def toList(self):
        out = []
        node = self
        while node:
            out.append(node.value)
            node = node.next

        return out


def removeConsecutiveSumTo0(head):
    visited = {}
    sum = 0

    node = head
    while node:
        sum += node.value
        visited[node.value] = node

        if sum == 0:
            head = node.next
            visited = {}
        elif sum in visited:
            visited[sum].next = node.next

        node = node.next

    return head
