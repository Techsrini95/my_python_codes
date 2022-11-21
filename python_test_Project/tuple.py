# tuple uses () and tuple is immutable  , we cant change values  ()
# lists [] are mutable we can change values / collection of elements []
# set - collection of unique elements {}
# dictionary when u have key & value  / keys should be unique & immutable  {}


tup = (21, 22, 39, 45, 56)      # tuple
lis = [12, 19, 44, 55, 66]      # list
lists = lis[1] = 33             # list updating at index 1 from 22 to 33 only works in list not in tuple
# tpp = tup[1]=33     #it wont works
sett = {11, 88, 22, 33, 44}     # index not support[1]
data = {1:'sri', 2:'raj', 3:'shi', 4:'abc'}  # keys
val = ['nav', 'bav', 'cav']  # keys
val2 = ['jee', 'kee', 'ree'] # values
comb= dict(zip(val, val2))   # dictionary create using zip
xex=comb['mon']='eed'         # if you add something into dictionary



print(lists)
print(lis)
print(tup)
print(sett)              # set won't get exact sequence ,but it uses hash concept
print(data [1])
print(data [2])
print(data.get(3))          # we can use get to print
print(data.get(10, 'NOT found'))
print(comb)
print(xex)

