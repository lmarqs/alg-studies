class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.visited = False

    def toList(self):
        out = []
        node = self
        while node:
            out.append(node.value)
            node = node.next

        return out


def remove_kth_from_linked_list(head, k):
    end = head
    for _ in range(k):
        end = end.next

    node = head
    prev = None

    while end:
        prev = node
        node = node.next
        end = end.next

    if node == head:
        return node.next

    prev.next = node.next

    return head
