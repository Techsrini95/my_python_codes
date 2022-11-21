# array -- all the values with same type ( don't have fixed list) ('b,B,u,h,H,i,I,L,f,d)

from array import *

vals = array('i', [5, 6, 3, 4])
new = array(vals.typecode, (a for a in vals))
new1 = array(vals.typecode, (a * a for a in vals))

print(vals)
print(vals.buffer_info())
print(vals[0])
print(vals.typecode)
print(new)
print(new1)

# ============================================
# create array from values from user

arr = array('i', [])

n = int(input('enter length array :'))

for i in range(n):
    x = int(input('enter values for :'))
    arr.append(x)

print(arr)

# =========================
# search for index number
val = int(input("enter values to search : "))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1


print(arr.index(val))
