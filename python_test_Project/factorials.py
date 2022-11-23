# factorials

def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
        print(f)


x = 5
fact(x)


#   ===========================
def fact(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f


x = 4
result = fact(x)

print(result)
