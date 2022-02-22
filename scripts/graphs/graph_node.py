"""
Node class for graphs, might need refactoring

Modifying node class for dijkstra's implementation.
Adding Edge class
18FEB22

Modifying Node class for Bellman Ford Algorithm
19FEB22

Modifying  Edge class for Kruskal Algorithm
Adding Vertex and KruskalNode class
Add vertex adjacency list for Primm Jarnik class
21FEB22
"""


class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.enqueued = False
        self.predecessor = None
        self.min_distance = float('inf')

    # Needed for heap less than comparison
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance


class Edge:

    def __init__(self, weight, start_node, target_node):
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class Vertex:

    def __init__(self, name):
        self.name = name
        self.node = None
        self.adjacency_list = []


class KruskalNode:

    def __init__(self, rank, node_id, parent=None):
        self.node_id = node_id
        self.parent = parent
        self.rank = rank
