""""Matthew Bono I. De las Alas
    DATALOG Lab16
    MAY. 09, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

""" Find an element in a Binary Search Tree

Define search(element) method. The method returns True if the element is present in
the BST otherwise returns False. In binary search trees: each left subtree is less than
or equal to its parent and each right subtree is greater than or equal to its parent.
Our tree can only store integer values. If the tree is empty, the method should return False.
"""

class Node:
    def __init__(self, element):
        self._element = element
        self._left = None
        self._right = None

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def getRoot(self):
        return self._root

    def traverse(self, node):
        if node != None:
            self.traverse(node._left)
            print(f'{node._element} ', end="") # No line feed to save screen area
            self.traverse(node._right)

    def add(self, element):
        # Add your code from Lab 13 here
        if self._root is None:  # if there is no root or the binary tree is empty
            self._root = Node(element)  # sets the root into the node
            self._size += 1  # increment since the length should increase by one every time an element is added
        else:
            self._add(element, self._root)  # if there is already a root in the binary tree
    pass

    def _add(self, element, node_current):
        if element < node_current._element:  # if the element is less than the value of the node
            if node_current._left is None:  # if the node does not have a value in left
                node_current._left = Node(element)  # sets the value left node into the new node
                self._size += 1  # increment since the length should increase by one every time an element is added
            else:
                self._add(element, node_current._left)  # if there is already a left node in the binary tree

        elif element > node_current._element:
            if node_current._right is None:  # if the element is greater than the value of the node
                node_current._right = Node(element)  # sets the value of the right node into the new node
                self._size += 1  # increment since the length should increase by one every time an element is added
            else:
                self._add(element, node_current._right)  # if there is already a right node in the binary tree
    pass

    def search(self, element):
        # Change code below this line
        return self._search(self._root, element)  # returns True or False if the element is present

    def _search(self, node_current, element):
        if node_current is None:  # if the node is not present or the Binary Search Tree has no values
            return False  # returns the value False
        elif element == node_current._element:  # if the value of the element is found in the Binary Search Tree
            return True  # returns the value True
        elif element < node_current._element:  # if the value of the element is less than the node in the binary Search Tree
            return self._search(node_current._left, element)  # returns the value of True or False until the element is found
        else:
            return self._search(node_current._right, element)  # returns the value of True or False until the element is found
        pass
    # Change code above this line



if __name__ == "__main__":
    myTree = BinaryTree()
    print(f'search(3): {myTree.search(3)}') # False
    myTree.add(26)
    myTree.add(10)
    myTree.add(31)
    myTree.add(5)
    myTree.add(15)
    myTree.add(28)
    myTree.add(29)
    print(f'length(): {len(myTree)}') # 7

    root = myTree.getRoot()
    print('traverse(): ', end=""); myTree.traverse(root); print("") # 5 10 15 26 29 31

    print(f'search(26): {myTree.search(26)}') # True
    print(f'search(21): {myTree.search(21)}') # False