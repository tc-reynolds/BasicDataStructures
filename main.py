from datastructures.stack import Stack
from datastructures.queue import Queue
from datastructures.max_heap import MaxHeap
from datastructures.linked_list import LinkedList

# This is a sample Python script.

def create_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    print(queue.dequeue())
    queue.print_queue()

def create_stack():
    stack = Stack([10, 12])
    stack2 = Stack()
    stack.push(3)
    stack.print_stack()
    stack2.print_stack()

def create_heap():
    heap = MaxHeap([10, 45, 22, 33])
    heap.push(65)
    heap.push(43)
    heap.push(100)
    print(heap.pop())
    print(heap.peek())
    heap.print_heap()

def create_linked_list():
    ll = LinkedList()
    ll.add(5)
    ll.add(3)
    ll.add(10)
    ll.remove(3)
    print(ll.find(5))
    ll.print_list()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_stack()
    create_queue()
    # create_heap()
    create_linked_list()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
