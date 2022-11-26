# constructor , self , heap memory
# constructor allows size of objects in heap memory
# constructor responsible to assign memory or calculate
# variables - instance , class(static)


class computer():

    def __init__(self):
        self.name = 'navin'
        self.age = 24

    def update(self):
        self.age = 33

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c1.age = 30
c2 = computer()
c2.name = 'badra'

c1.update()      # if i want for c2 i need to update as c2.update


if c1.compare(c2):
    print('they are same ')
else:
    print('they are diff')

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
print(id(c1))
print(id(c2))


# variables - instance , class(static)

class car():
    wheels = 4

    def __init__(self):  # instance variables (it will change on dependence)
        self.mil = 10
        self.com = 'BMW'


b1 = car()
b2 = car()

print(b1.mil, b1.com, b1.wheels)
print(b2.mil, b2.com, b2.wheels)
