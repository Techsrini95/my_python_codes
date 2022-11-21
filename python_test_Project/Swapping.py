# swapping variables a,b=b,a

a = 5
b = 7
x = 5
y = 7
m = 5
n = 7

temp = a
a = b
b = temp
# --------------------
x = x+y
y = x-y
x = x-y

m = m^n   # not waste extra bit
n = m^n
m = m^n

print(a)
print(b)
print(x)
print(y)
print(m)
print(n)


