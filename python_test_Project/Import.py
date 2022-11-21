# input
x = input('enter number 1')  # it takes automatically string
y = input('enter number 2')  # int(input('enter number 2'))
ch = input('enter characters')
ch1 = input('enter characters')[0]
expr = eval(input('enter expression'))  # eval evaluates math expression

z = x + y  # 12
a = int(x) + int(y)   # now it will work


print(z)   # 12
print(a)
print(ch[0])    # we want one char
print(ch)
print(ch1)
print(expr)
