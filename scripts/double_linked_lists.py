# Class Implementation & methods for double linked lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_nodes = 0
    
    def insert(self, data):
        # self.number_of_nodes += 1
        # new_node = Node(data)
        # # if no head node, insert as head node.
        # if not self.head:
        #     self.head = new_node
        # # if exists head node, insert before head node
        # else:
        #     new_node.next_node = self.head
        #     self.head = new_node
        pass

    def traverse_forward(self):
        # # start at the begining
        # actual_node = self.head

        # while actual_node is not None:
        #     print(actual_node.data)
        #     actual_node = actual_node.next_node
        pass

    def print_head(self):
        # print("head node: ", self.head.data)
        pass
    def print_head(self):
        # print("head node: ", self.head.data)
        pass

    def remove(self,data):
        # previous_node = None
        # actual_node = self.head
        # while actual_node.next_node is not None and actual_node.data != data:
        #     previous_node = actual_node
        #     actual_node = actual_node.next_node
        
        # if not actual_node:
        #     return

        # if not previous_node:
        #     self.head = actual_node.next_node
        # else:
        #     previous_node.next_node = actual_node.next_node
        pass

    def node_count(self):
        # print("current size of nodes: ", self.number_of_nodes)
        pass

if __name__=="__main__":
    # lltest = LinkedList()
    # lltest.insert_start(20)
    # lltest.print_head()
    # lltest.insert_start(31)
    # lltest.insert_start(99)
    # lltest.insert_start(72)
    # lltest.insert_start(1)
    # lltest.node_count()
    # lltest.traverse()
    # lltest.insert_start("Bob")
    # lltest.print_head()
    # lltest.remove(31)
    # lltest.insert_end(44)
    # lltest.remove("Bob")
    # lltest.insert_end(87)
    # lltest.insert_end(54)
    # lltest.traverse()