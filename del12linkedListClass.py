""""Matthew Bono I. De las Alas
    DATALOG Lab12
    APR. 28, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
""" Create a Linked List Class

Write an add method that assigns the first node you push to the linked list to the head; after that, 
whenever adding a node, every node should be referenced by the previous node's next property.

Note
Your list's length should increase by one every time an element is added to the linked list.
"""


class Node:
    def __init__(self, element=None):
        self._element = element
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def head(self):
        return self._head._element

    def traverse(self):
        current = self._head
        while current:
            print(f'{current._element} ', end="")
            current = current._next

    def add(self, element):
        # Change code below this line
        new = Node(element)  # assigning the variable new to the Node(element)
        if self._head is None:  # if the linked list has no head or empty
            self._head = new  # assigns the new node as the head of the Linked List
            self._size += 1  # increment since the list length increases every time an element is added to the linked

            return
        last = self._head  # assigns the variable last to the head
        while last._next:
            last = last._next  # assigns the variable last to the next element
        last._next = new  # assigns the last._next to new
        self._size += 1  # increment since the list length increases every time an element is added to the linked list
        pass
        # Change code above this line


if __name__ == "__main__":
    myLink = LinkedList()
    myLink.add('Mon')
    myLink.add('Tue')
    myLink.add('Wed')
    print(len(myLink))  # 3
    print(myLink.head())  # Mon
    myLink.traverse()  # Mon Tue Wed
