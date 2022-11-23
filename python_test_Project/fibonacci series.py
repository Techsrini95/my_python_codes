# add 1 & 2 nd number you will get  next (3rd) number
# 0 1 1 2 3 5 8 13 ......

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(a + b)


fib(9)
