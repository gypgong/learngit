# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# **map(映射)/reduce(归约)

''' 
#**map(映射)
r = map(function_to_apply, list_of_inputs)  
function_to_apply:代表函数
list_of_inputs:代表输入序列
r:结果是一个Iterator(迭代器)
将右侧的序列中元素，作为参数传入到左侧函数中，依次处理后生产新的iterator(迭代器)
map接收一个参数，第二个参数是iterable(可迭代对象)


# **reduce(归约)
reduce(function, iterable[, initializer]) 
function:代表函数
iterable:序列
initializer:初始值(可选)
reduce接收两个参数
'''

from functools import reduce
from collections.abc import Iterable, Iterator
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])

def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
reduce(fn, map(char2num, '13579'))

# 整理成一个str2int函数
from functools import reduce
DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(fn, s))

# 用 lambda 函数继续简化
from functools import reduce
DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print('='*30+'分割线'+'='*30)


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其它小写的规范名字。输入：['adam', 'LISA', 'barT'],输出：['Adam', 'Lisa', 'Bart']:

def normalize(name):
    if name and isinstance(name, str): # 是否为str
        name = name[0:1].upper() + name[1:].lower() # 切换大小写的函数
        return name 
        
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


print('='*30+'分割线'+'='*30)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    if L :
        for i in L:
            if isinstance(i, int) or isinstance(i, float):
                return reduce(lambda x, y: x*y, L)
    else:
        return None

# 测试
print('3 * 0.55 * 7 * 9 =', prod([3, 0.55, 7, 9]))
if prod([3, 0.55, 7, 9]) == 103.95:
    print('测试成功!')
else:
    print('测试失败!')


print('='*30+'分割线'+'='*30)


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    if s[0] != '-': # 正浮点数
        # i = s.index('.') # 找出'.'的index
        d = 10**(-(len(s) - s.index('.') -1)) # 确定小数点位置
        s = s[0:i] + s[i+1:] # s = [x for x in s if x != '.'] 列表生成式
    else: # 负浮点数
        s = s[1:] # 切掉'-'号（切片）
        # i = s.index('.')  # 找出'.'的index
        d = -(10**(-(len(s) - s.index('.') -1))) # 确定小数点位置，一并处理负数问题
        s = [x for x in s if x != '.']        
    def fn(x, y):
        return x * 10 + y
    def s2f(s):
        DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        return DIGITS[s]       
    return reduce(fn, map(s2f, s))*d

# 测试
print('str2float(\'-123.456\') =', str2float('-123.456'))
if abs(str2float('-123.456') - (-123.456)) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
