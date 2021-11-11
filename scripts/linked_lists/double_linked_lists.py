# Class Implementation & methods for double linked lists
from list_node import Node
import sys
sys.path.append(".")


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_nodes = 0

    def insert(self, data):
        self.number_of_nodes += 1
        new_node = Node(data)
        # # if no head node, insert as head node.
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # # if exists head node, insertion takes place after tail node O(n)
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def traverse(self, direction="forward"):
        # # start at the begining
        if direction == "forward":
            actual_node = self.head
            while actual_node is not None:
                print(actual_node.data)
                actual_node = actual_node.next_node
        elif direction == "backward":
            actual_node = self.tail
            while actual_node is not None:
                print(actual_node.data)
                actual_node = actual_node.prev_node
        else:
            print("direction to be specified : forward or backward traversal")

    def print_head(self):
        print("head node: ", self.head.data)

    def print_tail(self):
        print("tail node: ", self.tail.data)

    def remove(self, data):
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
        print("current size of nodes: ", self.number_of_nodes)


if __name__ == "__main__":
    lltest = DoubleLinkedList()
    lltest.insert(1)
    lltest.print_head()
    lltest.insert(2)
    lltest.insert(3)
    lltest.insert(4)
    lltest.node_count()
    lltest.insert(5)
    lltest.insert(6)
    lltest.insert(7)
    lltest.insert(8)
    lltest.insert(9)
    lltest.insert(10)
    lltest.node_count()
    lltest.traverse(direction="forward")
    lltest.print_head()
    lltest.traverse(direction="backward")
    # lltest.remove(31)
    # lltest.insert_end(44)
    # lltest.remove("Bob")
    # lltest.insert_end(87)
    # lltest.insert_end(54)
