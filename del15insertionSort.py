""""Matthew Bono I. De las Alas
    DATALOG Lab15
    MAY. 09, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
import operator  # import the operator function
""" Insertion Sort

Create an insSort(arr, mode) function that employs insertion sort algorithm to sort the elements in the
array arr. If mode is 0, sort in ascending order otherwise sort in descending order.

<https://www.geeksforgeeks.org/insertion-sort/>

Stay safe everyone!
"""


def insSort(arr, mode=0):  # function that employs insertion sort algorithm.
    # Insert code below this line
    for b in range(1, len(arr)):  # sets the range starting from 1 to the length of arr
        descend = operator.gt if mode else operator.lt  # sets the variable descend to the operator
        array_insert = arr[b]  # assigns the variable array_insert to the value off arr[b]
        a = b - 1  # assigns the variable a to the value of b - 1
        while 0 <= a and descend(array_insert, arr[a]):  # since a is greater than zero
            arr[a + 1] = arr[a]  # array
            a -= 1  # decrement
        arr[a + 1] = array_insert  # new value of array_insert
    return arr  # returns the value of insertion sort
    pass
    # Insert code above this line


if __name__ == '__main__':
    A = [-3, 64, 1, 25, 12, 59, 22, 26, 11]
    print(insSort(A))
    print(insSort(A, 1))

    B = ['one', 'two', 'too', '19', 'wuhan', 'three', 'covid', 'four', 'five', 'pass']
    print(insSort(B))
    print(insSort(B, 1))
