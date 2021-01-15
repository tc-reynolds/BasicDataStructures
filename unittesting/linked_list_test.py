import unittest
from datastructures.linked_list import LinkedList

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_add(self):
        self.ll.add(4)
        self.ll.add(10)
        self.assertEqual(self.ll.get_size(), 2)

    def test_remove(self):
        self.ll = LinkedList([5, 3, 10])
        self.assertEqual(self.ll.remove(5), True)
        self.assertEqual(self.ll.remove(233), False)

    def test_get_size(self):
        self.ll = LinkedList([5, 3, 12])
        self.assertEqual(self.ll.get_size(), 3)

    def test_find(self):
        pass




if __name__ == '__main__':
    unittest.main()
