class Stack:
    def __init__(self):
        self.values = []
    def push(self, item):
        self.values.append(item)
    def pop(self):
        if len(self.values) > 0:
            return self.values.pop()
        else:
            print("Empty Stack")
    def peek(self):
        if len(self.values) > 0:
            return self.values[-1]
        else:
            print("Empty Stack")
    def is_empty(self):
        return len(self.values) == 0
    def size(self):
        return len(self.values)