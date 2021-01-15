class Stack:
    def __init__(self, data=[]):
        self.data = data

    def pop(self):
        top = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        return top

    def peak(self):
        return self.data[len(self.data) - 1]

    def push(self, item):
        self.data.append(item)

    def get_size(self):
        return len(self.data)

    def print_stack(self):
        print(self.data)