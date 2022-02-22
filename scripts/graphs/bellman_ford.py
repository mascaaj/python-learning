"""
Bellman-Ford implementation
18FEB22
"""

import sys
sys.path.append(".")
from graph_node import Edge, Node


class BellmanFord:

    def __init__(self, vertex_list, edge_list, start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0
        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                u = edge.start_node
                v = edge.target_node
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance

        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("negative cycle detected")
                return

    def check_cycle(self, edge):
        if edge.start_node.min_distance + edge.weight < edge.target_node.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self, vertex):
        if not self.has_cycle:
            print("shortest path ", vertex.min_distance)
            actual_vertex = vertex
            while actual_vertex:
                print(actual_vertex.name)
                actual_vertex = actual_vertex.predecessor
        else:
            print("graph has negative cycle")


if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(9, node1, node5)
    edge3 = Edge(4, node2, node5)
    edge4 = Edge(12, node2, node3)
    edge5 = Edge(7, node2, node4)
    edge6 = Edge(3, node3, node4)
    edge7 = Edge(1, node3, node6)
    edge8 = Edge(9, node4, node7)
    edge9 = Edge(6, node5, node3)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(2, node6, node7)
    edge12 = Edge(6, node7, node3)
    # edge12 = Edge(-6, node7, node3)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    vertices = (node1, node2, node3, node4, node5, node6, node7, node8)
    edges = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12)
    bf = BellmanFord(vertices, edges, node1)
    bf.find_shortest_path()
    bf.get_shortest_path(node7)
