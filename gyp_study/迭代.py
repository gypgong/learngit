# !/usr/bin/env python3
# -*- coding: utf-8 -*-

dict1 = {11:'b', 2:'a', -3:'d', 4:'f', -5:'e'}

set1= {1, 2, 3, 'a', 'c', 'd', 'e',}


for i in set1:
    print(i)

dict1[1]

for i in dict1:
    print(i)

for i in dict1.values():
    print(i)

for i, e in dict1.items():
    print(i, e)


type('a')

# 迭代
''' 
如果给定一个list或tuple,我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
在Python中，迭代是通过for...in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如C代码：

for (i=0; i<length; i++) {
    n = list[i]
}

可以看出，Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其它可迭代对象上。
list这种数据类型虽然有下标，但很多其它数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代。
'''
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

'''  
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序可能很不一样。
默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values(),如果要同时迭代key和value,可以for k, v in d.items()。
由于字符串也是可迭代对象，因此，也可以作用于for循环：
'''

for c in 'annaamm':
    print(c)

''' 
所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其它数据类型。
那么如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

'''
from collections.abc import Iterable

isinstance('abc', Iterable) # str是否可以迭代

isinstance([1, 2, 3], Iterable) # list是否可迭代

isinstance((1, 2, 3), Iterable) # tuple是否可迭代

isinstance({'a':1, 'g':4, 'b': 0}, Iterable) # dict是否可迭代

isinstance({1, '2', 'c', 3, 5}, Iterable) # set是否可迭代

isinstance(124, Iterable)   # int是否可迭代

isinstance(12.4, Iterable)  # float是否可迭代



''' 
最后一个小问题，如果要对list实现类型Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

'''

list_2 = ['q', 2, 3, 4, 5, 6, 'sda', 'qwdqw',]
for i, v in enumerate(list_2):
    print(i, v)

# 上面的for循环里，同时引用了两个变量，在Python里很常见的，比如下面的代码：
for x, y in [(1,1),(2,3),(3,5)]:
    print(x, y)


# 练习
# 请使用迭代查找一个list中最小和最大的值

def findMinAndMax(L):
    if L == None:
       min = max = None       
    elif len(L) == 1:
       min = max = L[0]
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
    return (min, max) 


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
