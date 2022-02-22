"""
Primms Jarnik MST implementation
Uses edge definition that has start and target node instead of vertex
21FEB22
"""

import sys
import heapq
sys.path.append(".")
from graph_node import Edge, Vertex


class PrimmsJarnik:

    def __init__(self, unvisited_list):
        # if unvisited list length = 0, all have been visited
        self.unvisited_vertex = unvisited_list
        self.mst = []
        self.total_cost = 0
        self.heap = []

    def find_spanning_tree(self, start_vertex):
        """
        Pop from the heap
        Find all adjacent edges for unvisited target nodes
        Push to the heap
        """
        self.unvisited_vertex.remove(start_vertex)
        actual_vertex = start_vertex

        # while unvisited vertex is not empty
        while self.unvisited_vertex:
            # iterate thru all edges in the adjacency list
            for edge in actual_vertex.adjacency_list:
                # select edges which target vertex is has not been visited
                if edge.target_node in self.unvisited_vertex:
                    heapq.heappush(self.heap, edge)

            # remove smallest edge (lazy implementation)
            min_edge = heapq.heappop(self.heap)
            if min_edge.target_node in self.unvisited_vertex:
                self.mst.append(min_edge)
                print("mst addition : ", min_edge.start_node.name,
                      " - ", min_edge.target_node.name, " : ", min_edge.weight)
                self.total_cost += min_edge.weight
                actual_vertex = min_edge.target_node
                self.unvisited_vertex.remove(actual_vertex)

    def get_mst(self):
        return self.mst

    def get_cost(self):
        return self.total_cost


if __name__ == "__main__":

    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")

    edgeAB = Edge(2, vertexA, vertexB)
    edgeBA = Edge(2, vertexB, vertexA)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeEA = Edge(5, vertexE, vertexA)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeCA = Edge(6, vertexC, vertexA)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeFA = Edge(10, vertexF, vertexA)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeEB = Edge(3, vertexE, vertexB)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeDB = Edge(3, vertexD, vertexB)

    edgeCD = Edge(1, vertexC, vertexD)
    edgeDC = Edge(1, vertexD, vertexC)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeFC = Edge(2, vertexF, vertexC)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeED = Edge(4, vertexE, vertexD)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeGD = Edge(5, vertexG, vertexD)
    edgeFG = Edge(5, vertexF, vertexG)
    edgeGF = Edge(5, vertexG, vertexF)

    vertexA.adjacency_list.append(edgeAB)
    vertexA.adjacency_list.append(edgeAC)
    vertexA.adjacency_list.append(edgeAE)
    vertexA.adjacency_list.append(edgeAF)
    vertexB.adjacency_list.append(edgeBA)
    vertexB.adjacency_list.append(edgeBD)
    vertexB.adjacency_list.append(edgeBE)
    vertexC.adjacency_list.append(edgeCA)
    vertexC.adjacency_list.append(edgeCD)
    vertexC.adjacency_list.append(edgeCF)
    vertexD.adjacency_list.append(edgeDB)
    vertexD.adjacency_list.append(edgeDC)
    vertexD.adjacency_list.append(edgeDE)
    vertexD.adjacency_list.append(edgeDG)
    vertexE.adjacency_list.append(edgeEA)
    vertexE.adjacency_list.append(edgeEB)
    vertexE.adjacency_list.append(edgeED)
    vertexF.adjacency_list.append(edgeFA)
    vertexF.adjacency_list.append(edgeFC)
    vertexF.adjacency_list.append(edgeFG)
    vertexG.adjacency_list.append(edgeGD)
    vertexG.adjacency_list.append(edgeGF)

    unvisited_list = [vertexA, vertexB, vertexC, vertexD, vertexE, vertexF, vertexG]
    algorithm = PrimmsJarnik(unvisited_list)
    algorithm.find_spanning_tree(vertexD)
    print(algorithm.get_cost())
