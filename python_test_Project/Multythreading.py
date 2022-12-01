# multithreading

from threading import *
from time import *


class Hello(Thread):
    def run(self):
        for i in range(50):
            print('hello')
            sleep(.5)


class Hi(Thread):
    def run(self):
        for i in range(50):
            print('Hi')
            sleep(.5)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(.3)
t2.start()

t1.join()  # wait till t1 & t2 execute
t2.join()
print('bye')