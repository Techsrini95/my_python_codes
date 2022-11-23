# lambda anonymous function
from functools import reduce

x = lambda a: a * a

result = x(5)
print(result)

x = lambda a, b: a * b

result = x(3, 6)
print(result)

#  filter , map  , reduce

num = [2, 4, 6, 5, 77, 32, 33, 11, 22, 55, 67, 88]

evens = list(filter(lambda a: a % 2 == 0, num))
doubles = list(map(lambda a: a * 2, evens))
sum1 = reduce(lambda a, b: a + b, doubles)

print(evens)
print(doubles)
print(sum1)
