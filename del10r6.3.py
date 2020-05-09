""""Matthew Bono I. De las Alas
    DATALOG Lab09
    APR. 04, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

class ArrayStack: #class Array Stack

    def __init__(self): # initialization
        self._data = [] # using list to implement stacks, arrays

    def __len__(self):
        return len(self._data) # returns the length of the list

    def is_empty(self):
        return len(self._data) == 0 # function that returns if the stack is empty or not

    def push(self, e): # takes an element as an argument
        self._data.append(e) # appends the element

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() # removes the last item in the list

def transfer(S, T): # function with the signature transfer(S,T) to transfer elements from stack S to T, the element of the stack S
    for n in range(len(S)): # sets the range
        T.append(S.pop()) # append the elements of stack S into stack T
    return T # returns the value of T

# Main program to test the class ArrayStack and function transfer(S,T)
S = ArrayStack() # assigning the variable S for the first stack
S.push(10) # adds the element into the top of the stack [10]
S.push(20) # adds the element into the top of the stack [10,20]
S.push(30) # adds the element into the top of the stack [10, 20, 30]
S.push(40) # adds the element into the top of the stack [10,20,30,40]
S.push(50) # adds the element into the top of the stack [10,20,30,40,50]
S.push(60) # adds the element into the top of the stack [10,20,30,40,50,60]
S.push(70) # adds the element into the top of the stack [10,20,30,40,50,60,70]
S.push(80) # adds the element into the top of the stack [10,20,30,40,50,60,70,80]
S.push(90) # adds the element into the top of the stack [10,20,30,40,50,60,70,80,90]
S.push(100) # adds the element into the top of the stack [10,20,30,40,50,60,70,80,90,100]
print("Stack S: ")
print(S._data) # prints the data of the stack S
print("Number of items in the Stack: ")
print(len(S)) # prints the number of elements in the Stack S
T = [] # initializes an empty stack for Stack T
print("Stack T: ")
print(transfer(S,T)) # prints Stack T with the values of stack S which is transfered in reverse order
print("Number of items in the Stack: ")
print(len(T)) # prints the number of elements in the Stack T

