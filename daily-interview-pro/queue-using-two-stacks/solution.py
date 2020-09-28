class Queue:
    def __init__(self):
        self.enqueueStack = []
        self.dequeueStack = []

    def enqueue(self, val):
        self.enqueueStack.append(val)

    def dequeue(self):
        if len(self.dequeueStack) == 0:
            while len(self.enqueueStack) > 0:
                self.dequeueStack.append(self.enqueueStack.pop())

        return self.dequeueStack.pop()
