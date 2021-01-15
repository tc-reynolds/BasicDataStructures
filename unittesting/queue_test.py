import unittest
from datastructures.queue import Queue

class QueueTestCases(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(5)
        self.assertEqual(self.queue.get_queue()[0], 5)

    def test_dequeue(self):
        self.queue.enqueue(5)

        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.get_size(), 0)
        self.assertEqual(self.queue.dequeue(), False)

    def test_get_queue(self):
        self.queue.enqueue(4)
        self.assertEqual(len(self.queue.get_queue()), 1)

    def test_get_size(self):
        self.queue = Queue([4, 10, 3])
        self.assertEqual(self.queue.get_size(), 3)


if __name__ == '__main__':
    unittest.main()
