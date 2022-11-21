# pattern - end = ''

for i in range(4):
    print('# ', end='')

print()

for i in range(4):
    print('# ', end='')
print()

# ------------------------------------------------

for j in range(4):
    for i in range(4):
        print('$ ', end='')
    print()

# ----------------------------------

for k in range(4):
    for i in range(k + 1):
        print('@ ', end='')
    print()

# for else

nums = [12, 13, 25, 46, 55, 76]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('not found')
