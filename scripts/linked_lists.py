# Class Implementation & methods for linked lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0
    
    def insert_start(self, data):
        self.number_of_nodes += 1
        new_node = Node(data)
        # if no head node, insert as head node.
        if not self.head:
            self.head = new_node
        # if exists head node, insert before head node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self,data):
        self.number_of_nodes += 1
        new_node = Node(data)

        # start at the begining
        actual_node = self.head
        
        while actual_node.next_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse(self):
        # start at the begining
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def print_head(self):
        print("head node: ", self.head.data)
        print("head node reference", self.head.next_node)

    def delete_start(self):
        pass

    def node_count(self):
        return self.number_of_nodes

if __name__=="__main__":
    lltest = LinkedList()
    lltest.insert_start(20)
    lltest.print_head()
    lltest.insert_start(31)
    lltest.insert_start(99)
    lltest.insert_start(72)
    lltest.insert_start(1)
    lltest.insert_start("Bob")
    lltest.print_head()
    lltest.insert_end(44)
    lltest.traverse()