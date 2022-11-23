# class  (variables , attribute) and objects

class Computer():

    def conf(self):
        print('i5 , 16gb , 1tb')


comp1 = Computer()
comp2 = Computer()

Computer.conf(comp1)  # actual syntax
Computer.conf(comp2)
comp1.conf()  # works
comp1.conf()


#  special method init (initiate variables)


class laptop():
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('config is :', self.cpu, self.ram)


lap1 = laptop('i5', 16)
lap2 = laptop('rayen', 32)

lap1.config()
lap2.config()
