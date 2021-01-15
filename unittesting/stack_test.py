import unittest
from datastructures.stack import Stack


class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(5)
        self.stack.push(3)

        self.assertEqual(self.stack.get_size(), 2)
        self.assertEqual(self.stack.pop(), 3)

    def test_get_size(self):
        self.stack.push(5)

        self.assertEqual(self.stack.get_size(), 1)

        self.stack.pop()

        self.assertEqual(self.stack.get_size(), 0)

        self.stack.push(4)
        self.stack.push(-1)

        self.assertEqual(self.stack.get_size(), 2)

    def test_pop(self):
        self.stack = Stack([4, 5])
        item = self.stack.pop()

        self.assertEqual(item, 5)
        self.assertEqual(self.stack.peek(), 4)

        self.stack.pop()

        self.assertEqual(self.stack.pop(), False)


if __name__ == '__main__':
    unittest.main()
