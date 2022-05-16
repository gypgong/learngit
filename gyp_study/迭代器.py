# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# **迭代器
'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象。
'''
from collections.abc import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)
isinstance((), Iterable)

'''
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后爆出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
'''
from collections.abc import Iterator
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)
isinstance('abd', Iterator)

'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable
把list、dict、str等Iterable变成Iterator可以使用iter()函数
'''
isinstance(iter([]), Iterator)
isinstance(iter('abd'), Iterator)
isinstance(iter({'abd'}), Iterator)
isinstance(iter({'abd':1}), Iterator)

'''
为什么list、dict、str等数据类型不是Iterator?

这是因为Python的Iterator对象表示的对象是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，知道没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有
在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
'''

# **小结
'''  
# **凡是可作用于for循环的对象都是Iterable类型；
# **凡是可作用于next()函数的对象都是Iterator类型；它们表示一个惰性计算序列；
# **集合数据类型如 list、dict、str等都是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# **Python的for循环本质上就是通过不断调用next()函数实现的，例如：
'''

for x in [1, 2, 3, 4, 5]:
    pass
#  实际上完全等价于

# 首先获得Iterator对象
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break





from collections.abc import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


#**迭代器
#可迭代对象（可用for循环的对象）： 1.list、tuple、dict、set、str等几何数据类型。2.generator生成器，或者包含yield的生成器函数
from collections.abc import Iterable # Iterable 可迭代的对象
isinstance([],Iterable)   # True

#迭代器（Iterator）：可以被next()函数调用并不断返回下一个值的对象。生成器一定是迭代器对象
from collections.abc import Iterator # Iterator 迭代器
print(isinstance([],Iterator))  #False，虽然是可迭代对象，但不是迭代器
print(isinstance((x for x in range(100)),Iterator)) #True
print(isinstance([x for x in range(100)],Iterator)) #显然列表生成式不是迭代器

#关于Iterator，可以代表一个无穷集合，不确定长度。而list等并不是不确定长度。
l = (x for x in range(100)) #所以生成器对象，并不是一个长度为100的数据类型
print(len(l))  # TypeError: object of type 'generator' has no len()

#小结：
#1.凡是可以for的，都是可迭代对象。Iterable
#2.凡是可以调用next()函数的，都是迭代器对象。Iterator。表示一个惰性计算的序列
#3.python的for循环本质，就是不断调用next()实现的
def ange_for(i):
    it = iter(i)  # iter(i) 根据i获得一个Iterator对象
    while True:
        try:
            x = next(it)
        except StopIteration:
            break