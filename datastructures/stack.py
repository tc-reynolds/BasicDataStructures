class Stack:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def pop(self):
        if len(self.data) > 0:
            top = self.data[len(self.data) - 1]
            del self.data[len(self.data) - 1]
            return top
        else:
            return False

    def peek(self):
        return self.data[len(self.data) - 1]

    def push(self, item):
        self.data.append(item)

    def get_size(self):
        return len(self.data)

    def print_stack(self):
        print(self.data)
