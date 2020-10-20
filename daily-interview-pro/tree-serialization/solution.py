class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialize(root):
    if root == None:
        return '#'
    return str(root.val) + ' ' + serialize(root.left) + ' ' + serialize(root.right)


def deserialize(data):
    tree, _ = deserialize_rec(data.split(' '))
    return tree


def deserialize_rec(data, i=0):
    if data[i] == '#':
        return None, i

    v = int(data[i])
    l, i = deserialize_rec(data, i + 1)
    r, i = deserialize_rec(data, i + 1)

    return Node(v, l, r), i
