class Queue:
    def __init__(self, d=None):
        if d is None:
            self.data = []
        else:
            self.data = d

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if len(self.data) > 0:
            item = self.data[0]
            del self.data[0]
            return item
        else:
            return False

    def get_size(self):
        return len(self.data)

    def get_queue(self):
        return self.data

    def print_queue(self):
        print(self.data)
