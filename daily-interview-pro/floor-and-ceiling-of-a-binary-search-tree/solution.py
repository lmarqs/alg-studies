class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root, k, floor=None, ceil=None):
    if root != None:
        value = root.value

        if value == k:
            floor = ceil = value
        elif value > k:
            [floor, ceil] = findCeilingFloor(root.left, k, floor, value)
        elif value < k:
            [floor, ceil] = findCeilingFloor(root.right, k, value, ceil)
            
    return [floor, ceil]
