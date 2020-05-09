""""Matthew Bono I. De las Alas
    DATALOG Lab12
    APR. 28, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
""" Remove Elements from a Linked List

Write a remove method that takes an element and removes it from the linked list.
Notes:
The length of the list should decrease by one every time an element is removed from the linked list.
Include your add method from the previous exercise.
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
        print('')

    # include your add method here
    def add(self, element):
        new = Node(element)  # assigning the variable new to the Node(element)
        if self._head is None:  # if the linked list has no head or empty
            self._head = new  # assigns the new node as the head of the Linked List
            self._size += 1  # increment since the list length increases every time an element is added to the linked

            return
        last = self._head  # assigns the variable last to the head
        while last._next:
            last = last._next  # assigns the variable last to the next element
        last._next = new  # assigns the last._next to new
        self._size += 1  # increment since the list length increases every time an element is added to the linked lis
        pass

    def remove(self, element):
        # Change code below this line
        node_remove = self._head  # assigns the variable node_remove to the head
        if node_remove is not None:  # if there are elements in the linked list
            if node_remove._element == element:
                self._head = node_remove._next
                return
        while node_remove is not None:  # if the linked list has elements
            if node_remove._element == element:
                break
            prev = node_remove  # assigns the variable prev to the value of node remove
            node_remove = node_remove._next  #
        if node_remove is None:
            return False # if no element was found or the linked list is empty
        prev._next = node_remove._next
        pass
        # Change code above this line


if __name__ == "__main__":
    myLink = LinkedList()
    myLink.add('Mon')
    myLink.add('Tue')
    myLink.add('Wed')
    myLink.add(3)
    myLink.add('Thu')
    myLink.add('Fri')
    myLink.add(1)
    myLink.add('Sat')
    print(f'size = {len(myLink)}')  # size = 8
    print(f'head = {myLink.head()}')  # head = Mon
    myLink.traverse()  # Mon Tue Wed 3 Thu Fri 1 Sat
    myLink.remove('Mon')
    myLink.traverse()  # Tue Wed 3 Thu Fri 1 Sat
    myLink.remove(3)
    myLink.traverse()  # Tue Wed Thu Fri 1 Sat
    myLink.remove('Sat')
    myLink.traverse()  # Tue Wed Thu Fri 1
    myLink.remove('Wed')
    myLink.traverse()  # Tue Thu Fri 1
    print(myLink.remove('Sun'))  # False
    myLink.traverse()  # Tue Thu Fri 1
