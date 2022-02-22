"""
Dijkstra algorithm
18FEB22
"""
import sys
import heapq
sys.path.append(".")
from graph_node import Node, Edge


class Dijkstra:

    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        """
        Steps :
        1. Set start node min distance to 0
        2. Push start node onto heap
        3. Iterate till heap is not empty
        4. Pop the smallest value in heap
        5. check and update based on adjacency list and edge wt
        6. if st_nd_min_d + edge_weight < tgt_nd_min_d, update
        7. push updated info onto heap, ensure visited is true
        8. lazy implementation (binary heap) need to add guard
        so node is not revisited
        """
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            for edge in actual_vertex.adjacency_list:
                u = edge.start_node
                v = edge.target_node
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print("shortest path ", vertex.min_distance)
        actual_vertex = vertex
        while actual_vertex:
            print(actual_vertex.name)
            actual_vertex = actual_vertex.predecessor


if __name__ == "__main__":

    # Define the nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # Define the edges, with weights
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # define the adjacency list as edges
    # connected to the node
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    algorithm = Dijkstra()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node7)
