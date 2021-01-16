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
        # self.assertEqual(self.tree.find(12), 12)
        # self.assertEqual(self.tree.find(1231), False)

    def test_delete(self):
        pass

    def test_get_size(self):
        pass

    def test_preorder_traversal(self):
        pass

    def test_inorder_traversal(self):
        pass


if __name__ == '__main__':
    unittest.main()
