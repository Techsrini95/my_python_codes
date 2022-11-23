# types of arguments (actual & forml)
# actual ( position , keyword ,default ,variable length)

# position
def person(name, age):
    print(name)
    print(age)


person('srini', 27)


# keyword
def person(name, age):
    print(name)
    print(age)


person(age=23, name='srini')


# default
def person(name, age=18):
    print(name)
    print(age)


person('srini', 20)


# variable multiple values to add
def sum1(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)


sum1(99, 22, 31, 12, 27)
