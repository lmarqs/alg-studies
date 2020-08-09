class MaxStack:
    def __init__(self):
        self.max_stack = []
        self.stack = []

    def push(self, val):
        if self.max_stack:
            self.max_stack.append(max(self.max_stack[-1], val))
        else:
            self.max_stack.append(val)

        self.stack.append(val)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def max(self):
        return self.max_stack[-1]
