 #  lists (using square brackets) []
# nums=[12,34,99,06,03,67,44] #SyntaxError: leading zeros in decimal integer literals
                             #  are not permitted; use an 0o prefix for octal integers
                             #  we cant use 0 its an indentation error

numb=[12,34,67,44]   # without zero works
name =['srini','pavan','chetan']
integ = [1.9, 'pavan', 24]
values = [integ, name, integ]  # we can include numbers & integers
numb.append(94)
popo = numb.pop(1)
pope = numb.pop()

print(numb.extend([61,45,68,50]))  # it's not working in last line giving none
print(numb)
print(numb[1])
print(name)
print(integ)
print(values)
print(popo)
print(pope)



