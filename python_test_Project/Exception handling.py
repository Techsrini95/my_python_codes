# error -(compile error [syntax] ,logical error [wrong output] , run time error[ zero divide like cases ]

a = 5
b = 3

try:
    print('open resource ')
    print(a / b)
    k = int(input('enter values :'))
    print(k)

except ZeroDivisionError as e:
    print('error with  zero :', e)

except ValueError as e:
    print('Invalid Input :', e)

except Exception as e:
    print('Something went wrong :', e)

finally:
    print('closed resource ')
