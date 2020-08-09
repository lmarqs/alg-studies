class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        out = str(self.value)
        if self.left:
            out += self.left.preorder()
        if self.right:
            out += self.right.preorder()
        return out


def invert(node):
    if node:
        right = node.right
        left = node.left

        node.right = invert(left)
        node.left = invert(right)

    return node
