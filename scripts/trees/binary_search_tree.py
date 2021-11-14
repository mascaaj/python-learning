"""
Binary search tree implemntation
"""

import sys
sys.path.append(".")
from tree_node import Node


class BinarySearchTree:

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
            self.root = Node(data, None)
            # print("check for populated root ",self.root.data)
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
                node.leftChild = Node(data, node)
        else:
            # print("insert as rightChild ", node.data, data)
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

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


class TreeComparator:

    def compare_trees(self, node1, node2):
        """
        Base cases:
            if node1 and node2 are none
            nodes are not equal, return false
        """
        # print("node1 data", node1.data)
        # print("node2 data", node2.data)
        if not node1 or not node2:
            return node1 == node2

        if node1.data is not node2.data:
            return False

        # Recursively check left and right nodes
        left_same = self.compare_trees(node1.leftChild, node2.leftChild)
        right_same = self.compare_trees(node1.rightChild, node2.rightChild)
        return left_same and right_same


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(30)
    bst.insert(-1000)
    bst.insert(3)
    bst.insert(-4000)
    bst.insert(-5000)
    bst.insert(80)
    bst.insert(900)
    bst.insert(12)
    bst.insert(2)
    bst.insert(6)
    bst.insert(11)
    bst.insert(15)
    bst.traverse()
    # print("min item %s" % bst.get_min_value())
    # print("max item %s" % bst.get_max_value())
    bst.remove(12)
    bst.traverse()

    bst3 = BinarySearchTree()
    bst4 = BinarySearchTree()

    bst3.insert(10)
    bst3.insert(5)
    bst3.insert(13)
    bst3.insert(25)
    bst3.insert(11)

    bst4.insert(10)
    bst4.insert(5)
    bst4.insert(13)
    bst4.insert(25)
    bst4.insert(11)
    comparator = TreeComparator()
    print("are identical trees ? :", comparator.compare_trees(bst3.root, bst4.root))
