#!/usr/bin/env python
# coding=utf-8

import math

''' 
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''

a = int(input('a = '))
b = int(input('b = '))

print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

a += b
a *= a + 2
print(a)

print("--------------------------------------")
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)

print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)

print(flag1 is True)
print(flag2 is not False) 

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius 
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)

