# pass list of number  i need even / odd different
def count():
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            # print('even')
            even += 1
        else:
            odd += 1

    return even, odd


lst = [20, 21, 19, 34, 55, 63, 11, 9, 4, 7]
even, odd = count()

print(even)
print(odd)

print('even : {} and odd : {}'.format(even,odd))

