class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(root):
    if root == None:
        return 0

    if root.val == '+':
        return evaluate(root.left) + evaluate(root.right)
    if root.val == '-':
        return evaluate(root.left) - evaluate(root.right)

    if root.val == '/':
        return evaluate(root.left) / evaluate(root.right)

    if root.val == '*':
        return evaluate(root.left) * evaluate(root.right)
    
    return root.val
