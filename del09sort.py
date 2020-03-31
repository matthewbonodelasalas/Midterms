""""Matthew Bono I. De las Alas
    DATALOG Lab09
    MAR. 28, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

def insertion_sort(A): # defining the function to sort strings
    for k in range(1,len(A)): # range from 1 to n-1
        cur = A[k] # element to be inserted
        j = k # find correct j index for current
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1 #decrement
        A[j] = cur # cur is placed in its right place
string_sort = ['D','o','n','B','o','s','c','o','T','e','c','h','n','i','c','a','l','C','o','l','l','e','g','e'] # Sorting the string "DonBoscoTechnicalCollege"
insertion_sort(string_sort) # using the insertion_sort function to sort the given string
print("String sort: ")
print(''.join(string_sort)) # prints the sorted string Uppercase letters comes first in the sort while the lowercase letters comes after



