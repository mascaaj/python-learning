"""
Kruskal Algorithm example implementation
20FEB22
"""

import sys
# import math
sys.path.append(".")
from graph_node import Edge, KruskalNode, Vertex


class DisjointSet:

    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        # list of representatives for a node
        self.root_nodes = []
        # make disjoint sets from the vertex_list
        self.make_sets()

    def make_sets(self):
        for v in self.vertex_list:
            node = KruskalNode(0, len(self.root_nodes))
            # Link node to the vertex
            v.node = node
            self.root_nodes.append(node)

    def find(self, node_id):
        """
        Return with representative of the tree
        Find the node
        Find the representative
        Path compression for all nodes
        """
        current_node = node_id
        while current_node.parent:
            # iterate up the tree till root
            current_node = current_node.parent

        root = current_node
        current_node = node_id

        # apply path compression for all nodes
        while current_node.parent:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        """
        find representative (root_node)
        identify root node in root_node list
        check rank parameter
        merge
        update rank
        """
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        # find node return id, need to find
        # actual node from root node list
        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            # if ranks are equal, merge and bump rank
            root2.parent = root1
            root1.rank += 1


class Kruskal:

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def find_mst(self):
        disjoint_set = DisjointSet(self.vertex_list)
        mst = []

        self.edge_list.sort()
        for edge in self.edge_list:
            # these should be vertices, but it shares implementation
            u = edge.start_node
            v = edge.target_node

            if disjoint_set.find(u.node) is not disjoint_set.find(v.node):
                mst.append(edge)
                disjoint_set.merge(u.node, v.node)

        for edge in mst:
            print(edge.start_node.name, " - ", edge.target_node.name,
                  " : ", edge.weight)


if __name__ == "__main__":

    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")
    vertex8 = Vertex("H")

    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]
    ka = Kruskal(vertices, edges)
    ka.find_mst()
