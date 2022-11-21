# numpy  (array , line space ,logspace ,arange ,zeros ,ones)
from numpy import *

arr = array([23, 45, 66, 67.4], int)  # it can convert if we don't mention ,or we can mention
arr1 = linspace(0, 20, 5)  # divide into equal parts
arr2 = logspace(1, 2, 3)
arr3 = arange(1, 30, 2)
arr4 = logspace(0, 10, 5)
arr5 = zeros(5)
arr6 = arr + 5
grr = arr.view()  # copt -- shalo copy , deep copy
grr2 = arr.copy()

grr1 = arr * 2


ttype = arr.dtype
print(arr)
print(ttype)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print('%.2f' % arr4[2])
print(arr5)
print(arr6)
print(grr)
