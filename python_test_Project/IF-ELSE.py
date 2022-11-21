# IF - ELSE
x = int(input('enter number :'))
r = x % 2
s = x % 3
print(r)
print(s)
# ======================================== simpl
if True:
    print('yes')
# =========================================== query
if r == 0:
    print('even')
else:
    print('odd')
# ========================================== nested query
if s == 0:
    print('odd')
    if x > 5:                     # nested query
        print('great')
    else:
        print('not great')
else:
    print('even')
# ========================================= else if (elif)
if x == 1:
    print('one')
if x == 2:
    print('Two')
if x == 3:
    print('Three')
if x == 4:
    print('Four')
else:
    print('no match')  # working for all conditions need to chk
# ======================================================================
if x == 1:
    print('one')
elif x == 2:
    print('Two')
elif x == 3:
    print('Three')
elif x == 4:
    print('Four')
elif x == 5:
    print('Five')
else:
    print('no match')
