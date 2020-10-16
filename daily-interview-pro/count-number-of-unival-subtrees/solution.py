class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(root):
    c = 1

    if root.right != None:
        c += count_unival_subtrees(root.right)

    if root.left != None:
        c += count_unival_subtrees(root.left)

    if root.left != None and root.right != None:
        if root.left.val == root.val and root.right.val == root.val:
            c -= 2

    return c
