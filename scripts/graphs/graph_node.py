"""
Node class for graphs, might need refactoring
"""


class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.enqueued = False
