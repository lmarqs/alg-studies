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


def intersection(a, b):
    node = a

    while node:
        node.visited = True
        node = node.next

    node = b
    while node:
        if(node.visited):
            return node

        node = node.next


    return a
