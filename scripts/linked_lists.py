# Class Implementation & methods for linked lists
import sys
import os
import time
sys.path.append(".")

from list_node import Node

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

    def remove(self,data):
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

if __name__=="__main__":

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
        for i in range(50000):
            lltest.insert_start(i)
        time_stop = time.time()
        lltest.node_count()
        delta_time = time_stop-time_start
        print("Delta time for linked list insertion", delta_time)

        array=[]
        time_start = time.time()
        for i in range(50000):
            array.insert(0 , i)
        time_stop = time.time()
        lltest.node_count()
        delta_time = time_stop-time_start
        print("Delta time for list insertion", delta_time)