# global & local variables
a = 10


def something():
    a = 15
    print('inside', a)


something()
print('outside', a)

# use global
a = 10


def something():
    global a
    a = 15
    print('g-inside', a)


something()
print('g-outside', a)

# ========================================= we want local and want to change global
a = 10
b = 9
c = 6

print(id(a))


def something():
    a = 15
    x = globals()['a']
    print(id(x))
    print('d-inside', a)


something()
print('d-outside', a)
