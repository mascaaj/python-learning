"""
Node implementation for trees
This class has been created for BST
"""


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
