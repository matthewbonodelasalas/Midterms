""""Matthew Bono I. De las Alas
    DATALOG Lab15
    MAY. 09, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
""" Selection Sort

Create a selSort(arr, mode) function that employs selection sort algorithm to sort the elements in the
array arr. If mode is 0, sort in ascending order otherwise sort in descending order.

<https://www.geeksforgeeks.org/selection-sort/>

Stay safe everyone!
"""


def selSort(arr, mode=0):  # function that employs selection sort algorithm
    # Insert code below this line
    if len(arr) <= 1:  # if length of arr is less than or equal to 1
        return arr  # returns the value of arr
    for b in range(len(arr)):  # sets the range
        element_swap = b  # assigns the variable element_swap to = b
        for y in range(b + 1, len(arr)):  # sets the range
            if mode and arr[y] > arr[element_swap] or not mode and arr[y] < arr[element_swap]:
                element_swap = y  # assigns the variable element_swap to y
        arr[b], arr[element_swap] = arr[element_swap], arr[b]  # swapping elements of array
    return arr  # returns the value of arr
    pass
    # Insert code above this line


if __name__ == '__main__':
    A = [-3, 64, 1, 25, 12, 59, 22, 26, 11]
    print(selSort(A))
    print(selSort(A, 1))

    B = ['one', 'two', 'too', '19', 'wuhan', 'three', 'covid', 'four', 'five', 'pass']
    print(selSort(B))
    print(selSort(B, 1))