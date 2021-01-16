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
        #Checks for duplicate
        if self.data == data:
            return False
        if self.data > data:
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
        if self.data == data:
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



