class minStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        if not self.minStack or x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

        self.stack.append(x)

    def pop(self):
        self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
