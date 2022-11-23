# kwargs -- keyworded length variables

def person(name, *data):
    print(name)
    print(data)


person('srini', 23, 98765, 'mumbai')  # here not specified the variables (don't know what is the data  )


# name =srini  , age =23  ........

def person(name, **data):  # ** used to get
    print(name)
    print(data)


person('srini', age=23, mob=98765, city='mumbai')


# name =srini  , age =23  ........ line by line

def person(name, **data):  # ** used to get
    print(name)
    for i, j in data.items():
        print(i, j)


person('srini', age=23, mob=98765, city='mumbai')
