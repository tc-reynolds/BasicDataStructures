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
        self.root = r
        #If User inits with list, this will convert it to a linked list
        if isinstance(r, list):
           self.read_list_into_ll(r)
        elif r is not None:
            self.root = r
            ++self.size
        else:
            self.root = r

    def read_list_into_ll(self, ls):
        #Handles if Linked List already exists
        if isinstance(self.root, Node) is False:
            self.root = Node(ls[0])
            self.size = 1
        if len(ls) > 1:
            for data in ls[1:]:
                node = Node(data)
                self.add(node)
                ++self.size
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
                    --self.size
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

