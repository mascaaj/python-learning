"""
Node implementation for trees
This class has been created for BST
"""


class Color:
    RED = 1
    BLACK = 2


class BSTNode:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


class AVLNode(BSTNode):

    def __init__(self, data, parent):
        super().__init__(data, parent)
        self.height = 0


class RBNode(BSTNode):

    def __init__(self, data, parent, color=Color.RED):
        super().__init__(data, parent)
        self.color = color
