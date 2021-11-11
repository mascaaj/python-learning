# Class Implementation & methods for linked lists
from list_node import Node

import sys
import time
sys.path.append(".")


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

    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        print("Middle Node data : ", slow_pointer.data)

    def reverse(self):
        current_node = self.head
        prev_node = None
        next_node = None
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def insert_end(self, data):
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

    def remove(self, data):
        previous_node = None
        actual_node = self.head
        while actual_node.next_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if not actual_node:
            return

        if not previous_node:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

    def node_count(self):
        print("current size of nodes: ", self.number_of_nodes)


if __name__ == "__main__":

    test_name = "timing_tests"
    lltest = LinkedList()

    if test_name == "functional_tests":
        lltest.insert_start(20)
        lltest.print_head()
        lltest.insert_start(31)
        lltest.insert_start(99)
        lltest.insert_start(72)
        lltest.insert_start(1)
        lltest.node_count()
        lltest.traverse()
        lltest.insert_start("Bob")
        lltest.print_head()
        lltest.remove(31)
        lltest.insert_end(44)
        lltest.remove("Bob")
        lltest.insert_end(87)
        lltest.insert_end(54)
        lltest.traverse()

    elif test_name == "timing_tests":
        time_start = time.time()
        for i in range(100):
            lltest.insert_start(i)
        time_stop = time.time()
        lltest.traverse()
        # lltest.node_count()
        lltest.get_middle_node()
        print("reversing linked list")
        lltest.reverse()
        lltest.traverse()
        lltest.get_middle_node()
        delta_time = time_stop - time_start
        print("Delta time for linked list insertion", delta_time)
