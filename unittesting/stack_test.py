import unittest
from datastructures.stack import Stack


class StackTestCase(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(5)
        stack.push(3)
        stack.print_stack()
        self.assertEqual(2, stack.get_size())

    def test_get_size(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.get_size(), 1)
        stack.push(6)
        self.assertEqual(stack.get_size(), 2)

    def test_pop(self):
        stack = Stack([4, 5])
        item = stack.pop()
        self.assertEqual(item, 5)
        self.assertEqual(stack.peak(), 4)


if __name__ == '__main__':
    unittest.main()
