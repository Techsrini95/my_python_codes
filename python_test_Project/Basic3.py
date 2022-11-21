# addresses  -id
# data types  (none,numeric,list,tuple,set,string,range,dictionary / mapping)
# numeric(int,float,complex,bool)   true=1 , false=0
a = 10
b = 15
ab = 11  # int
ac = 'srinivas'  # string
ad = 2.5  # float
ae = 6 + 9j  # complex
s = int(ad)  # conversion from one data type to another 2.5 to 2 float to int
t = complex(ab, ad)
boo = a > b
boo2 = a < b
li = [12, 13, 14, 15]
tu = (23, 24, 25, 26)
se = {33, 34, 35, 36}
st = 'sting data'
rng = range(0, 11)    # range is used for iteration
lst = list(range(0, 10))  # to list the values in range  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = list(range(0, 22, 2))    # to give difference is 2
dic = {'srini': 'samsung', 'pavan': 'mi', 'gana': 'BlackBerry'}     # keys assign to values for dictionary /mapping
dk = dic.keys()                                                     # to check keys
dv = dic.values()                                                   # to check values
dg = dic['srini']                                                   # to check ant particular  values
dg1 = dic.get('pavan')                                              # to check particular values using get


print(id(a))     # 140704252089416 address of 10
print(id(b))     # 140704252089576
print(type(a))
print(type(ab))
print(type(ae))
print(s)
print(t)
print(boo)
print(boo2)                 # bool-ion operator
print(int(True))
print(int(False))
print(type(li))           # data types for all
print(type(tu))
print(type(se))
print(type(st))
print(type(rng))
print(lst)
print(lst2)
print(dic)
print(dk)            # to know keys in dictionary
print(dv)            # to know values in dictionary
print(dg)
print(dg1)
