import unittest
from datastructures.max_heap import MaxHeap


class MaxHeapTestCases(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()

    def test_push(self):
        self.heap.push(5)
        self.assertEqual(self.heap.get_heap(), [5])

    def test_peek(self):
        self.heap.push(5)
        self.assertEqual(self.heap.peek(), 5)

        self.heap.push(10)
        self.heap.push(32)
        self.heap.push(-23)
        self.assertEqual(self.heap.peek(), 32)

    def test_pop(self):
        self.heap.push(5)
        self.assertEqual(self.heap.pop(), 5)

        self.heap.push(5)
        self.heap.push(10)
        self.heap.push(15)
        self.heap.push(3)
        self.assertEqual(self.heap.pop(), 15)


if __name__ == '__main__':
    unittest.main()
