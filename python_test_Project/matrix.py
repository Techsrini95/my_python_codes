# matrix & function
from numpy import *


def matrix1():
    arr = array([
        [1, 2, 3, 4, 5, 6]
        , [7, 5, 8, 3, 6, 9]
    ])
    arr2 = arr.flatten()
    arr3 = arr2.reshape(2, 6)
    arr4 = arr2.reshape(2, 2, 3)
    m = matrix(arr2)
    m1 = matrix('1,2,3; 4, 5, 6; 9,11,67')
    print(arr)
    print(arr2)
    print(arr3)
    print(arr4)
    print(m)
    print(m1)


matrix1()
