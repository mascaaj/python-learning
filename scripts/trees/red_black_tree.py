"""
Red black tree implemntation
Copied from binary search tree implementation

@todo
15NOV21
Clean up methods and prototypes
Add violation handling <- rotation & recoloring

15FEB22
Complete & tested
"""

import sys
sys.path.append(".")
from tree_node import Color, RBNode


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        cases :
        1. check if root node, insert as root
        2. if not, root, insert_node
        """
        if not self.root:
            print("root empty")
            self.root = RBNode(data, None)
            self.settle_violation(self.root)
        else:
            self.insert_node(data, self.root)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def traverse(self):
        """
        cases:
        Check for root node existance
            if it does not exist, break
        If it does, begin traversal
        """
        if self.root:
            self.traverse_in_order(self.root)
        else:
            print("No data exists for traversal")

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def insert_node(self, data, node):
        """
        cases
            1. Check if the data is larger or smaller than the parent node
            2. if smaller, insert as left child, else as right child
            3. before insertion check if left child exists else add left child
            4. if exists, insert recursively
        """
        if data < node.data:
            # print("insert as leftChild ", node.data, data)
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = RBNode(data, node)
                self.settle_violation(node.leftChild)
        else:
            # print("insert as rightChild ", node.data, data)
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = RBNode(data, node)
                self.settle_violation(node.rightChild)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

    def remove_node(self, data, node):
        """
        cases:
            0. Return if the node is empty
            1. Find the given node, using traversal/ simple search
                - if greater, right child
                - if lesser, left child
                - else found node
            2. Removal cases
                1. Leaf node, no children
                    - Find parent node
                    - Tell check if node is right or left child
                    - remove reference to node (assign none)
                    - delete node
                2. middle node, single child
                    - Find parent node (if not none)
                    - Check if node to be deleted has left child or right child (node.avaliableChild)
                    - Check if the node to be deleted is left or right child of parent (parent.avaliableChild)
                    - assign parent.AvaliableChild to node.avaliableChild
                    - if parent node is none, assign to root node
                    - assign the joined node to the correct parent
                    - delete node
                3. middle node, two children (or a root node)
                    - find predecessor
                    - swap data with node to be deleted
                    - swapped node becomes leaf node, remove leaf node
        """
        # check if node is none & return
        if not node:
            return

        if data < node.data:
            print("left check", node.data, data)
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            print("right check", node.data, data)
            self.remove_node(data, node.rightChild)
        else:
            print("node found", node.data)
            # leaf node removal
            if not node.leftChild and not node.rightChild:
                parent = node.parent
                print("enter leaf node deletion")
                if parent and parent.rightChild == node:
                    parent.rightChild = None
                    print("deleting right child")
                elif parent and parent.leftChild == node:
                    parent.leftChild = None
                    print("deleting left child")
                elif parent is None:  # <- key edge case
                    print("deleting root node")
                    self.root = None
                del node

            # middle node with one child, left
            elif node.leftChild and not node.rightChild:
                # Untested
                # node to be deleted has left child

                parent = node.parent
                if parent:
                    # check if parent node relationship is left or right child
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                else:
                    self.root = node.leftChild
                del node

            # middle node with one child, right
            elif not node.leftChild and node.rightChild:
                # Untested
                # node to be deleted has right child

                parent = node.parent
                if parent:
                    # check if parent node relationship is left or right child
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                else:
                    self.root = node.rightChild
                del node

            # middle node with 2 children
            elif node.leftChild and node.rightChild:
                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        """
        Essentially a get max function
        """
        if node.rightChild:
            return self.get_predecessor(node.rightChild)

        return node

    def rotate_right(self, node):
        """
        Update references
        Set new parent
        update parent
        """
        # update references
        print("rotating to the right on node :", node.data)
        temp_left_node = node.leftChild
        t = temp_left_node.rightChild
        temp_left_node.rightChild = node
        node.leftChild = t

        # inform child about new parent assignment
        if t:
            t.parent = node
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        # update parent about new child assignment
        # First check if head node, next check if node reference was left or right
        if temp_left_node.parent and temp_left_node.parent.leftChild == node:
            temp_left_node.parent.leftChild = temp_left_node
        if temp_left_node.parent and temp_left_node.parent.rightChild == node:
            temp_left_node.parent.rightChild = temp_left_node

        # root node assignment
        if node == self.root:
            self.root = temp_left_node

    def rotate_left(self, node):
        """
        Update references
        Set new parent
        update parent
        """
        # update references
        print("rotating to the left on node :", node.data)
        temp_right_node = node.rightChild
        t = temp_right_node.leftChild
        temp_right_node.leftChild = node
        node.rightChild = t

        # inform child about new parent assignment
        if t:
            t.parent = node
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        # update parent about new child assignment
        # First check if head node, next check if node reference was left or right
        if temp_right_node.parent and temp_right_node.parent.leftChild == node:
            temp_right_node.parent.leftChild = temp_right_node
        if temp_right_node.parent and temp_right_node.parent.rightChild == node:
            temp_right_node.parent.rightChild = temp_right_node

        # root node assignment
        if node == self.root:
            self.root = temp_right_node

    def is_red(self, node):
        if not node:
            return False
        return node.color == Color.RED

    def settle_violation(self, node):
        """
        1. Check for uncle status and its right/left childness
        2. Match the 4 cases
        3. recolor / rotate as necessary
        """
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            parent_node = node.parent
            grandparent_node = parent_node.parent

            if grandparent_node.leftChild == parent_node:
                uncle_node = grandparent_node.rightChild
                # case 1 & 4, recoloring
                if uncle_node and self.is_red(uncle_node):
                    print("case 1 or 4")
                    print("recoloring grandparent node", grandparent_node.data)
                    grandparent_node.color = Color.RED
                    print("recoloring parent node", parent_node.data)
                    parent_node.color = Color.BLACK
                    print("recoloring uncle node", uncle_node.data)
                    uncle_node.color = Color.BLACK
                    node = grandparent_node
                else:
                    # Uncle node exists and is black, rotation, recoloring
                    if node == parent_node.rightChild:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    parent_node.color = Color.BLACK
                    print("recoloring parent node", parent_node.data)
                    grandparent_node.color = Color.RED
                    print("recoloring grandparent node", grandparent_node.data)
                    self.rotate_right(grandparent_node)
            else:
                uncle_node = grandparent_node.leftChild
                # case 1 & 4, recoloring
                if uncle_node and self.is_red(uncle_node):
                    print("case 1 or 4")
                    print("recoloring grandparent node", grandparent_node.data)
                    grandparent_node.color = Color.RED
                    print("recoloring parent node", parent_node.data)
                    parent_node.color = Color.BLACK
                    print("recoloring uncle node", uncle_node.data)
                    uncle_node.color = Color.BLACK
                    node = grandparent_node
                else:
                    # Uncle node exists and is black, rotation, recoloring
                    if node == parent_node.leftChild:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    parent_node.color = Color.BLACK
                    print("recoloring parent node", parent_node.data)
                    grandparent_node.color = Color.RED
                    print("recoloring grandparent node", grandparent_node.data)
                    self.rotate_left(grandparent_node)

        if self.is_red(self.root):
            print("coloring root to black")
            self.root.color = Color.BLACK


if __name__ == "__main__":

    rbt = RedBlackTree()
    rbt.insert(32)
    rbt.insert(10)
    rbt.insert(55)
    rbt.insert(1)
    rbt.insert(19)
    rbt.insert(79)
    rbt.insert(16)
    rbt.insert(23)
    rbt.insert(12)
    rbt.traverse()
