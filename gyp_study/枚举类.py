# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)




from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# @unique 装饰器可以帮助我们检查保证没有重复的值
# 访问这些枚举类型可以有若干种方法：
 
 day1 = Weekday.Mon

