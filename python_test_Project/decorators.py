# irrespective of sequence it should take numerator bigger than denominator

def dev(a, b):
    print(a/b)


def smart_dev(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


dev = smart_dev(dev)

dev(8, 4)
