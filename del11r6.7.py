""""Matthew Bono I. De las Alas
    DATALOG Lab11
    APR. 17, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

class ArrayQueue: #ArrayQueue class
    DEFAULT_CAPACITY = 10 # sets the default capacity to 10

    def __init__(self): # initialization
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self): # function that returns the number of elements
        return self._size

    def is_empty(self): # function that determines if the queue is empty
        return self._size == 0 # returns True if the queue is empty

    def first(self): # function that return the element at the front of the queue
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self): # remove and return the first element of the queue

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e): # add element to the back of the queue

        if self._size == len(self._data):
            self._resize(2 * len(self.data)) # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1 # increment

    def _resize(self, cap):

        old = self._data # keep track of existing list
        self._data = [None] * cap # allocate list with new capacity
        walk = self._front
        for k in range(self._size): # sets the range
            self._data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulos
        self._front = 0 # front has been realigned

# Main Program to test classArrayQueue
a = ArrayQueue() # assigning the variable a to ArrayQueue()
print("Sequence of operations: ")
print("enqueue(5),enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue() ") # prints the sequence of operations
print("dequeue(),enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6)") # prints the sequence of operations
print("dequeue(),dequeue(), enqueue(4), dequeue(), dequeue() ") # prints the sequence of operations
print("Values returned: ")
print(a.enqueue(5)) # adds the element 5 into the back of the queue [5]
print(a.enqueue(3)) # adds the element 3 into the back of the queue [5,3]
print(a.dequeue()) # removes and retruns the first element of the queue which is 5
print(a.enqueue(2)) # adds the element 2 into the back of the queue [3,2]
print(a.enqueue(8)) # adds the element 8 into the back of the queue [3,2,8]
print(a.dequeue()) # removes and retruns the first element of the queue which is 3
print(a.dequeue()) # removes and retruns the first element of the queue which is 2
print(a.enqueue(9)) # adds the element 9 into the back of the queue [8,9]
print(a.enqueue(1)) # adds the element 1 into the back of the queue [8,9,1]
print(a.dequeue()) # removes and retruns the first element of the queue which is 8
print(a.enqueue(7)) # adds the element 7 into the back of the queue [9,1,7]
print(a.enqueue(6)) # adds the element 6 into the back of the queue [9,1,7,6]
print(a.dequeue()) # removes and retruns the first element of the queue which is 9
print(a.dequeue()) # removes and retruns the first element of the queue which is  1
print(a.enqueue(4)) # adds the element 4 into the back of the queue [7,6,4]
print(a.dequeue()) # removes and retruns the first element of the queue which is 7
print(a.dequeue()) # removes and retruns the first element of the queue which is 6

