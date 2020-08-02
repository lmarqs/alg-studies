class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def toString(self):
        node = self
        output = ''

        while node != None:
            output += str(node.val)
            output += " "
            node = node.next

        return output

    def reverseIteratively(self):
        lastChangedNode = self
        nodeToChangeNext = lastChangedNode.next
        lastChangedNode.next = None

        while nodeToChangeNext != None:
            nextNodeToVisit = nodeToChangeNext.next
            nodeToChangeNext.next = lastChangedNode
            lastChangedNode = nodeToChangeNext
            nodeToChangeNext = nextNodeToVisit

        return lastChangedNode

    def reverseRecursively(self, prev=None):
        head = self.next.reverseRecursively(self) if self.next != None else self
        self.next = prev
        return head
