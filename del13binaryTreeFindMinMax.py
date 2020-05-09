""""Matthew Bono I. De las Alas
    DATALOG Lab13
    MAY. 01, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

""" Find the Minimum and Maximum Value in a Binary Search Tree

Define two methods, findMin and findMax. These methods should return the minimum and maximum value held in the
binary search tree. In binary search trees: each left subtree is less than or equal to its parent and each right
subtree is greater than or equal to its parent. Our tree can only store integer values. If the tree is empty,
either method should return None.
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
            print(f'{node._element} ', end="")  # No line feed to save screen area
            self.traverse(node._right)

    # Include your add method here
    def add(self, element):
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

    # Change code below this line
    def findMin(self):
        if self._root is not None:  # if the Binary Search Tree has values or root
            current_node = self._root  # assigns the variable current_node to the value of self._root
            while current_node._left is not None:  # if there is a node in the left
                current_node = current_node._left  # assigns the variable current_node to the value of current_node._left
            return current_node._element  # returns the minimum value of the Binary Search Tree
        pass

    def findMax(self):
        if self._root is not None:  # if the Binary Search Tree has values or root
            current_node = self._root  # assigns the variable current_node to the value of self._root
            while current_node._right is not None:  # if there is a node in the right
                current_node = current_node._right  # assigns the value of current_node to the value of current_node._right
            return current_node._element  # returns the maximum value of the Binary Search Tree

        pass
    # Change code above this line


if __name__ == "__main__":
    myTree = BinaryTree()
    print(f'findMin(): {myTree.findMin()}')
    print(f'findMax(): {myTree.findMax()}')
    myTree.add(26)
    myTree.add(10)
    myTree.add(31)
    myTree.add(5)
    myTree.add(15)
    myTree.add(28)
    myTree.add(29)
    print(f'length(): {len(myTree)}')  # 7

    root = myTree.getRoot()
    print('traverse(): ', end="");
    myTree.traverse(root);
    print("")  # 5 10 15 26 29 31

    print(f'findMin(): {myTree.findMin()}')
    print(f'findMax(): {myTree.findMax()}')
