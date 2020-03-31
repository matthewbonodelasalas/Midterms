""""Matthew Bono I. De las Alas
    DATALOG Lab08
    MAR. 27, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

import sys  # for the getsizeof() function to be provided
data = []  # empty list
for k in range(27):  # sets the range
    a = len(data)  # Number of elements
    b = sys.getsizeof(data)  # actual size of data in bytes
    print('Length:{0:3d};Size in bytes:{1:4d}'.format(a, b))  # prints the length and size of data in bytes
    data.append(None)  # increase length by 1
