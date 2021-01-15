class Queue:
    def __init__(self, d=[]):
        self.data = d

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        item = self.data[0]
        del self.data[0]
        return item

    def get_size(self):
        return len(self.data)

    def print_queue(self):
        print(self.data)
