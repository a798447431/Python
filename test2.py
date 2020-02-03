#!/usr/bin/env python
# coding=utf-8
'''
str = raw_input("按下enter键退出, 其他任意键显示...\n")
print str
'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x = "a"
y = "b"

print x
print y

print '_________'
print x,
print y,

print x, y

counter = 100
miles = 1000.0
name = "John"

print counter
print miles 
print name

a = b = c = 1
d, e, f = 4, 5, "john"
print a, b, c ,d ,e, f

'''
python 有五个标准的数据类型
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
'''

var1 = 1
var2 = 10 

del var1
#print var1
print var2

str = 'Hello World'

print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list 
print list[0]
print list[1:3]
print list[2:]
print tinylist * 2
print list + tinylist

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple
print tuple[0]
print tuple[1:3]
print tuple[2:]
print tinytuple * 2
print tuple + tinytuple

#tuple[2] = 1000 
list[2] = 1000

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values() 


