class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)
