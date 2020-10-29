from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalancedBST(nums):
    return createBalancedBSTHelper(nums, 0, len(nums) - 1)


def createBalancedBSTHelper(nums, start, end):
    if start == end:
        return Node(nums[start])

    middle = (start + end) // 2

    return Node(nums[middle],
                createBalancedBSTHelper(nums, start, middle - 1),
                createBalancedBSTHelper(nums, middle + 1, end))
