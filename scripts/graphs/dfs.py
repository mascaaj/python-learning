"""
Depth first search implementation for graphs
1. using user defined stack implementation
2. using recusrsion and inbuilt operation stack
# differs from course implementation, had to add enqueued flag
"""

import sys
sys.path.append("../stacks_queues")
from stacks import Stack
from graph_node import Node


def depth_first_search(start_node):
    stack = Stack()
    stack.push(start_node)

    while not stack.is_empty():
        print("Current Stack size : ", stack.size())
        actual_node = stack.pop()
        print("Popping Node : ", actual_node.name)
        actual_node.visited = True

        for n in actual_node.adjacency_list:
            if not n.visited and not n.enqueued:
                print(n.name)
                stack.push(n)
                n.enqueued = True


def depth_first_search_recursion(node):

    node.visited = True
    print(node.name)

    for n in node.adjacency_list:
        if not n.visited:
            depth_first_search(n)


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    node3.adjacency_list.append(node5)
    node3.adjacency_list.append(node4)
    node3.adjacency_list.append(node2)

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node7)

    node4.adjacency_list.append(node8)
    node4.adjacency_list.append(node1)

    node5.adjacency_list.append(node4)
    node5.adjacency_list.append(node8)

    node6.adjacency_list.append(node4)

    node7.adjacency_list.append(node6)
    node8.adjacency_list.append(node7)
    node8.adjacency_list.append(node6)

    depth_first_search_recursion(node3)
