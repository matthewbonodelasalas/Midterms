""""Matthew Bono I. De las Alas
    DATALOG Lab08
    MAR. 27, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

import sys  # for the getsizeof() function to be provided
data = []  # empty list
c = 0  # sets the value of c to zero
for k in range(27):  # sets the range
    a = len(data)  # Number of elements
    b = sys.getsizeof(data)  # actual size of data in bytes
    data.append(None)  # length by 1
    if a > 0 and b > c:
        c = b  # c is equals to b
        print('Value of k: {0}'.format(a - 1))  # prints the sequence of array capacities


