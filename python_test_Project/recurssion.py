# recursion & factorial recursion
# calling function from itself

import sys

sys.setrecursionlimit(10)

print(sys.setrecursionlimit(10))

i = 0


def greet():
    global i
    i = i + 1
    print('hello srini', i)
    greet()


greet()


# factorial recursion

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


result = fact(5)

print(result)
