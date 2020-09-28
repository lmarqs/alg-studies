class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


def deepest(node):
    if node == None:
        return None, 0

    ln, ld = deepest(node.left)
    rn, rd = deepest(node.right)

    if ln == None and rn == None:
        return node, 1

    if ld > rd:
        return ln, ld + 1

    return rn, rd + 1
