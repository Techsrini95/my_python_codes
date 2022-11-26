# types of methods (instance , static , class)
# instances   - accessor , mutators
class students:
    school = 'srinivas'

    def __init__(self, m1, m2, m3, m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4

    def avg(self):  # instance s1 ,s2 call
        return (self.m1 + self.m2 + self.m3 + self.m4) / 4

    @classmethod
    def info_get(cls):
        return cls.school

    @staticmethod
    def info():
        print('abc modules ......')


s1 = students(12, 33, 44, 55)
s2 = students(55, 66, 22, 11)

print(s1.avg())  # instance s1 ,s2 call
print(s2.avg())

print(s1.m1, s1.m2, s1.m3, s1.m4)
print(s2.m1, s2.m2, s2.m3, s2.m4)
print(students.info_get())
students.info()


# class inside class (inner class )

class candidates:  # outer class

    def __init__(self, name, rolnm):
        self.name = name
        self.rolnm = rolnm
        self.lap = self.laptop

    def show(self):
        print(self.name, self.rolnm)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'

        def show(self):
            print(self.brand, self.cpu)


w1 = candidates('srini', 23)
w2 = candidates('pavan', 44)

w1.show()
w2.show()

