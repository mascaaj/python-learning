import sys
import os
import time
sys.path.append("../scripts/linked_lists")

from linked_lists import LinkedList
from double_linked_lists import DoubleLinkedList

if __name__=="__main__":

    max_size = 500000
    array=[]
    lltest = LinkedList()
    dlltest = DoubleLinkedList()

    time_start = time.time()
    for i in range(max_size):
        lltest.insert_start(i)
    time_stop = time.time()
    lltest.node_count()
    delta_time = time_stop-time_start
    print("Delta time for linked list insertion", delta_time)

    time_start = time.time()
    for i in range(max_size):
        dlltest.insert(i)
    time_stop = time.time()
    dlltest.node_count()
    delta_time = time_stop-time_start
    print("Delta time for double linked list insertion", delta_time)

    time_start = time.time()
    for i in range(max_size):
        array.insert(0 , i)
    time_stop = time.time()
    print("current array size : ", len(array))
    delta_time = time_stop-time_start
    print("Delta time for list insertion", delta_time)