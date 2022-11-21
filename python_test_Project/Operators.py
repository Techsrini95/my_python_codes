# operators (Arithmetic ,Assignment ,Relational ,logical, unary operators)
# Arithmetic (+ ,-,*,/,==, ** )
# Assignment - need to do increment  a=b ,a*=b , a,b =b,a
# unary operator   n=-n
# relational operator (< ,>,<= ,>= ,!=)
# logical operator    and , or , xor , not - negate  ( a>1 and b<2 ,a> or b<2 , not x )

# number system conversion  decimal  , binary , hexadecimal , octal
# binary - (base 2) [ convert decimal to binary ] bin(n)
# octal  - (base 8 [0-7])   ( oct(n) )
# hexadecimal  - 0-16 ( base 16 { 0-9 a-f} )  (hex(N) )

a = 24
b = 30
c = bin(a + b)
d = 0b110011       # binary to decimal  '0b'
e = oct(25)
f = 0o32
g = hex(32)
h = 0xf
i = 0x334

print(bin(a))        # 0b11000
print(bin(b))        # 0b11110
print(c)             # 0b11110
print(d)             # 25
print(e)             # 0o31
print(f)             # 26
print(g)             # 0x20
print(h)             # 15
print(i)             # 820
