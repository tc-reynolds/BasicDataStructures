class BST:

    def __init__(self, data, left=None, right=None):
        if isinstance(data, list):
            self.data = data[0]
            del data[0]
            self.insert_list(data)
        else:
            self.data = data
        self.left = left
        self.right = right

    def insert_list(self, ls):
        for data in ls:
            self.insert(data)

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = BST(data)
                return True
        elif self.data < data:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = BST(data)
                return True

    def find(self, data):
        if self.data is None:
            return False
        elif self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left is None and self.right is not None:
            return 1 + self.right.get_size()
        elif self.left is not None and self.right is None:
            return 1 + self.left.get_size()
        elif self.left is None and self.right is None:
            return 1

    def min_value_node(self, parent):
        if self.left is None:
            return [self, parent]
        else:
            return self.left.min_value_node(self)

    def delete(self, root, key):
        if root is None:
            return root
        elif root.data < key:
            root.right = root.delete(root.right, key)
        elif root.data > key:
            root.left = root.delete(root.left, key)
        else:
            # Case 1, No Child
            if root.right is None and root.left is None:
                if root.data == key:
                    root.data = None
            # Case 2, One Child
            elif self.left is None and self.right is not None:
                root = self.right
            elif self.left is not None and self.right is None:
                root = self.left
            else:
                next_highest, parent = self.right.min_value_node(root.right)
                root.data = next_highest.data
                root.right = self.delete(parent.right, next_highest.data)
        return root

    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res

