# break continue pass
av = 4
x = int(input('enter num candy :'))
i = 1
j = 1
k = 1
while i <= x:
    print('CANDY')
    i += 1

# break
while j <= x:
    if j > av:
        print('out of stock')
        break
    print('sweet')
    j = j + 1
print('thank you')

# continuous
for k in range(60, 80):  # here input won't work because for loop use range
    if k % 3 == 0:
        continue
    print(k)

for k in range(60, 80):  # here input won't work because for loop use range
    if k % 3 == 0 or k % 5 == 0:
        continue
    print(k)

# pass - need to print even numbers

for s in range(100, 150):
    if s % 2 != 0:
        continue
    print(s)

# need to print odd numbers

for o in range(200, 250):
    if o % 2 == 0:
        continue
    print(o)

for n in range(0, 101):
    if n % 2 == 0:
        pass
    else:
        print(n)

