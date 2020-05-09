""""Matthew Bono I. De las Alas
    DATALOG Lab12
    APR. 28, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

""" Search within a Linked List

Write an isEmpty method that checks if the linked list is empty,
an indexOf method that returns the index of a given element, and
an elementAt that returns an element at a given index.
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

    # Change code below this line
    def isEmpty(self):
        while self._size == 0:
            return True
        else:
            return False
        pass

    def indexOf(self, element):
        current = self._head
        search_element = element  # assigns the variable search_element into the given element to find the index
        found = False  # sets the value of found into False
        count = 0  # initializes the count to zero since the list always starts counting at aero
        while current != None and not found:
            if current._element == search_element:
                found = True  # if the element is found in the linked list
                return count  # returns the index of the given element in the  linked list
            else:
                current = current._next  # assigns the variable current to the value of current._next
                count += 1  # increment
        if current == None and found == False:
            return -1  # returns the value -1 if the given element is not found in the linked list

    pass

    def elementAt(self, at):
        current = self._head  # assigns the variable current to the value of self._head
        count = 0  # initializes the count to zero since the list always starts counting at zero
        while current:
            if count == at:
                return current._element  # returns the value of the element at the given index
            count += 1  # increment
            current = current._next
        return None  # if the element in the linked list is not found

    pass
    # Change code above this line


if __name__ == "__main__":
    myLink = LinkedList()
    print(myLink.isEmpty())  # True
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
    print(myLink.isEmpty())  # False
    print(myLink.indexOf('Mon'))  # 0
    print(myLink.indexOf('Sat'))  # 7
    print(myLink.indexOf('Sun'))  # -1
    print(myLink.elementAt(0))  # Mon
    print(myLink.elementAt(1))  # Tue
    print(myLink.elementAt(6))  # 1
    print(myLink.elementAt(-1))  # None
    print(myLink.elementAt(8))  # None
