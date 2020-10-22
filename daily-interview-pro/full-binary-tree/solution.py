from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1
            if len(q):
                result += "\n"

        return result


def fullBinaryTree(node):
    if node.left == None and node.right == None:
        return node

    if node.left == None:
        return fullBinaryTree(node.right)

    if node.right == None:
        return fullBinaryTree(node.left)

    node.left = fullBinaryTree(node.left)
    node.right = fullBinaryTree(node.right)

    return node
