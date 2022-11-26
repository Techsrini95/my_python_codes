# polymorphism - poly - morph  (duck typing ,operator overloading, method overloading, method overriding)
class pycharm:  # duck type

    def execute(self):
        print('running ......')
        print('compiling ......')


class laptop:
    def sode(self, ide):
        ide.execute()


ide = pycharm()
lap1 = laptop()

lap1.sode(ide)


# operator overloading (+ ,- ,*)

class students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = students(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.m1, self.m2)  # override ride str with integer


s1 = students(43, 54)
s2 = students(55, 66)

s3 = s1 + s2

print(s3.m1)

if s1 > s2:
    print('wins')
else:
    print('loose')

print(s1)  # because of override its giving number else it will give address as taking it default as string


# method over loading & over ridding

class book:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def sum(self, a=None, b=None, c=None):
        x = 0
        if a != None and b != None and c != None:
            x = a + b + c
        elif a != None and b != None:
            x = a + b
        return x


x1 = book(21, 33)
x2 = book(21, 33)
print(x1.sum(22, 66, 76))
print(x2.sum(22, 66))


# over riding

class notesA:
    def show(self):
        print('NOTES A')


class notesB(notesA):
    pass  # if we run you will get error


class notesb(notesA):  # override
    def show(self):
        print('NOTES B')


na = notesA()
na1 = notesb()
na2 = notesB()

na.show()
na1.show()
na2.show()
