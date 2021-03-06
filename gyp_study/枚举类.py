# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum
from tkinter import W
from webbrowser import MacOSX

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)




from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique 装饰器可以帮助我们检查保证没有重复的值
# 访问这些枚举类型可以有若干种方法：
 
day1 = Weekday.Mon

print(day1)

print(Weekday.Tue)

print(Weekday['Tue'])

print(Weekday.Tue.value)

print(day1 == Weekday.Mon)

print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))

# Weekday(7) #报错 ValueError




for name, member in Weekday.__members__.items():
    print(name, '=>', member)



# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过～！')
else:
    print('测试失败～！')

