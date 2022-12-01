# files

f = open('mydata', 'r', )

# print(f.read())

print(f.readline(), end='')
print(f.readline())

# write
f1 = open('abc', 'w')   # append

f1.write('first line ')
f1.write('first second ')
f1.write('third file ')
