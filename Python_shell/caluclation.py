Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=6
y=8
x+y
14
_+y
22
name = 'hibdh'
name
'hibdh'
name + 'rocks'
'hibdhrocks'
name +'   bkdfv'
'hibdh   bkdfv'
x= 'production house '
x
'production house '
 x[1]
 
SyntaxError: unexpected indent
>>> names='youtube rocks'
>>> names
'youtube rocks'
>>> names[1]
'o'
>>> names[3]
't'
>>> names[12]
's'
>>> names[-4]
'o'
>>> names[1]='r'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    names[1]='r'
TypeError: 'str' object does not support item assignment
>>> nums=[12,34,22,44,77]
>>> nums.append[44]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    nums.append[44]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums
[12, 34, 22, 44, 77]
>>> 
>>> nums.append[88]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nums.append[88]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums
[12, 34, 22, 44, 77]
>>> nums.append(88)
>>> nums
[12, 34, 22, 44, 77, 88]
>>> nums.insert(29)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    nums.insert(29)
TypeError: insert expected 2 arguments, got 1
nums.insert(3,29)
nums
[12, 34, 22, 29, 44, 77, 88]
nums.sort
<built-in method sort of list object at 0x000001DFBF2FA540>
nums
[12, 34, 22, 29, 44, 77, 88]
nums.reverse
<built-in method reverse of list object at 0x000001DFBF2FA540>
nums.remove(34)
nums
[12, 22, 29, 44, 77, 88]
nums.pop(3)
44
nums.copy()
[12, 22, 29, 77, 88]
nums
[12, 22, 29, 77, 88]
nums.extend(23)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    nums.extend(23)
TypeError: 'int' object is not iterable
nums
[12, 22, 29, 77, 88]


nums.pop()
88
nums.extend([77,87,26,69])
nums
[12, 22, 29, 77, 77, 87, 26, 69]
nums.pop()
69
