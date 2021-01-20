import unittest
from datastructures.binary_state_tree import BST

class BSTTestCases(unittest.TestCase):
    def setUp(self):
        self.tree = BST(5)

    def test_insert(self):
        self.assertEqual(self.tree.insert(3), True)
        self.assertEqual(self.tree.find(3), 3)

        self.assertEqual(self.tree.insert(4), True)
        self.assertEqual(self.tree.find(4), 4)

        self.assertEqual(self.tree.insert(4), False)
        self.assertEqual(self.tree.find(4), 4)


    def test_insert_list(self):
        self.tree.insert_list([5, 3, 1, 4, 7, 9])


    def test_find(self):
        self.tree.insert_list([4, 10, 12, 3])
        self.assertEqual(self.tree.find(3), 3)
        self.assertEqual(self.tree.find(12), 12)
        self.assertEqual(self.tree.find(1231), False)

    def test_delete(self):
        # self.tree.insert_list([10, 12, 3, 0, 4])
        self.assertEqual(self.tree.find(5), 5)
        self.tree.delete(self.tree, 5)
        self.assertEqual(self.tree.find(5), False)

        self.tree.insert(5)
        self.assertEqual(self.tree.find(5), 5)


    def test_in_order_traversal(self):
        self.tree.insert_list([3, 10, 12, 15, 19])
        sorted_list = self.tree.in_order_traversal(self.tree)
        self.assertEqual(sorted_list[0], 3)
        self.assertEqual(sorted_list[-1], 19)


    def test_get_size(self):
        # Test no insert but init
        self.assertEqual(self.tree.get_size(), 1)

        # Test single insert
        self.tree.insert(3)
        self.assertEqual(self.tree.get_size(), 2)

        # Test multiple inserts
        self.tree.insert(15)
        self.tree.insert(-2)
        self.tree.insert(0)
        self.assertEqual(self.tree.get_size(), 5)

        # Test Duplicate
        self.tree.insert(15)
        self.assertEqual(self.tree.get_size(), 5)

    def test_min_value_node(self):
        self.assertEqual(self.tree.min_value_node(self.tree)[0].data, 5)

        self.tree.insert(3)
        self.assertEqual(self.tree.min_value_node(self.tree)[0].data, 3)

        self.tree.insert(-12)
        self.tree.insert(-4)
        self.tree.insert(0)
        self.tree.insert(101)
        self.tree.insert(-10)
        self.assertEqual(self.tree.min_value_node(self.tree)[0].data, -12)



    def test_preorder_traversal(self):
        pass

    def test_inorder_traversal(self):
        pass



if __name__ == '__main__':
    unittest.main()
