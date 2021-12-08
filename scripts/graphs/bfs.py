"""
Breadth first search implementation for graphs
# differs from course implementation, had to add enqueued flag
"""

import sys
sys.path.append("../stacks_queues")
from queues import Queue
from graph_node import Node


def breadth_first_search(start_node):
    queue = Queue()
    queue.enqueue(start_node)

    while not queue.is_empty():
        print(queue.size())
        actual_node = queue.dequeue()
        actual_node.visited = True

        for n in actual_node.adjacency_list:
            if not n.visited and not n.enqueued:
                print(n.name)
                queue.enqueue(n)
                n.enqueued = True


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    node3.adjacency_list.append(node2)
    node3.adjacency_list.append(node4)
    node3.adjacency_list.append(node5)

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node7)

    node4.adjacency_list.append(node1)
    node4.adjacency_list.append(node8)

    node5.adjacency_list.append(node4)
    node5.adjacency_list.append(node8)

    node6.adjacency_list.append(node4)

    node7.adjacency_list.append(node6)
    node8.adjacency_list.append(node7)
    node8.adjacency_list.append(node6)

    breadth_first_search(node3)
