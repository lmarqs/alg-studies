from collections import deque


class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    if not preorder or not inorder:
        return None

    val = preorder[0]
    idx = inorder.index(val)

    left = reconstruct(preorder[1:idx+1], inorder[:idx])
    right = reconstruct(preorder[idx+1:], inorder[idx+1:])

    return Node(val, left, right)
