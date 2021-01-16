import unittest
from datastructures.linked_list import LinkedList

class LinkedListTestCases(unittest.TestCase):
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

        self.ll = LinkedList()
        self.assertEqual(self.ll.get_size(), 0)

        self.ll.add(5)
        self.ll.add(12)
        self.ll.read_list_into_ll([3, 4, 5])
        self.assertEqual(self.ll.get_size(), 5)


    def test_find(self):

        self.assertEqual(self.ll.find(3), False)

        self.ll = LinkedList([10, 2, 5, 1])
        self.assertEqual(self.ll.find(10).data, 10)
        self.assertEqual(self.ll.find(1).data, 1)
        self.assertEqual(self.ll.find(3), False)

        self.ll.remove(10)
        self.assertEqual(self.ll.find(10), False)

        self.ll.add(4)
        self.assertEqual(self.ll.find(4).data, 4)




if __name__ == '__main__':
    unittest.main()
