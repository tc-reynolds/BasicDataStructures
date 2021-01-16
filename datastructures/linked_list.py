class Node:

    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p


    def __str__(self):
        return '(' + str(self.data) + ')'

class LinkedList:

    def __init__(self, r=None):
        self.size = 0
        self.root = None
        #If User inits with list, this will convert it to a linked list
        if isinstance(r, list):
           self.read_list_into_ll(r)
        elif r is not None:
            self.root = r
            self.size += 1
        else:
            self.root = r

    def read_list_into_ll(self, ls):
        if self.root is None or isinstance(self.root, Node) is False:
            self.root = Node(ls[0])
            self.size += 1
            del ls[0]
        #Handles if Linked List already exists
        for data in ls:
            self.add(data)

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                    self.size -= 1
                    return True
                else:
                    self.root = this_node.next_node
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return this_node
            else:
                this_node = this_node.next_node
        return False

    def get_list_data(self):
        ll_data = []
        this_node = self.root
        while this_node is not None:
            ll_data.append(this_node.data)
            this_node = this_node.next_node
        return ll_data

    def get_size(self):
        return self.size

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print("None")
