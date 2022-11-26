# inheritance (oops) parent & child relationship

class A:
    def features1(self):
        print('features1 is working ')

    def features2(self):
        print('features2 is working ')


class B:
    def features3(self):
        print('features3 is working ')

    def features4(self):
        print('features4 is working ')


class C(A, B):
    def features5(self):
        print('features5 is working ')


a1 = A()
b1 = B()
c1 = C()

a1.features1()
a1.features2()
c1.features5()


# constructor in inheritance (MRO)


class X:
    def __init__(self):
        print('init of x ')

    def features1(self):
        print('featuresX1 is working ')

    def features2(self):
        print('featuresX2 is working ')


class Y:
    def __init__(self):
        super().__init__()
        print('init of y ')  # if we don't have init y it will choose x one

    def features3(self):
        print('featuresY3 is working ')

    def features4(self):
        print('featuresY4 is working ')


class Z(X):
    def __init__(self):
        super().__init__()  # super will help to fetch both child & parents init
        print('init of z ')

    def features4(self):
        print('featuresz4 is working ')


class G(Y, X):
    def __init__(self):
        super().__init__()  # MRO - when you have 2 init then it will choose left one
        print('init of g ')

    def features4(self):
        print('featuresg4 is working ')


# x1 = X()
y1 = Y()
z1 = Z()
g1 = G()
