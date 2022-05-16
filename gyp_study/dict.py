# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#  dict (dictionary)
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 使用 dict 实现，只需要一个‘名字’ -‘成绩’的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])

# 数据存入dict的方法，除了初始化时指定，还可以通过key放入：
d['Adam'] = 67
print(d['Adam'])

# 由于一个key只能对应一个value,所以，多次对一个key放入value,后面的值会把前面的值冲掉:
d['jack'] = 90
print('Jack\'s scores:', d['jack']) 

d['jack'] = 88
print('Jack\'s scores:', d['jack'])

# 如果key不存在，dict就会报错：
# print('Thomas\'s scores:', d['Thomas']) 
''' KeyError: 'Thomas'新的报错学习,key错误 '''

# 要避免key不存在的错误，有两种方法，一是通过 in 判断key是否存在：
print('Thomas' in d)
# 二是通过 dict 提供的get()方法， 如果key不存在，就可以返回 None ,或者自己指定的value:
print(d.get('Thomas'))
print(d.get('Thomas', '没有对应的key'))

# 注意返回 None 的时候Python的交互环境不显示结果

# 要删除一个key, 用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)

''' 和 list 比较, dict 有以下几个特点：
    1.查找和插入的速度极快,不会随key的增加而变慢;
    2.需要展示大量的内存,内存浪费多 
    
    而 list 相反：
    1.查找和插入的时间随着元素的增加而增加
    2.占用空间小，浪费内存很少
    
    所以, dict 是用空间来换时间的一种方法
dict 可以用在需要高速查找的很多地方,在Python代码中几乎无处不在,需要牢记的第一条就是 dict 的key必需是不可以变的对象
这是因为 dict 根据key来计算value的存储位置,如果每次计算相同的key得出不同的结果,那 dict 内部就完全混乱了.这个通过key计算位置的算法成为哈希算法(Hash)
要保住hash的正确性,昨晚key的对象就不能变,在Python中,字符串、整数等都是不可以变的,因此,可以放心的昨晚key,而list是可以变的,就不能作为key:'''
# key = [1, 2, 3]
# d[key] = 'a list'
# TypeError: unhashable type: 'list'

dict_1 = {(1, 3): ['xiaozhang']}
print(dict_1)

# set
''' set 和 dcit 类似,也是一组key的集合,但不存储value.由于key不能重复,所以,在 set 中, 没有重复的key
要创建一个 set , 需要提供一个 list 作为输入集合'''
s = set([1, 1, 2, 3, 2, 3])
print(s)

# 通过add(key)方法可以添加元素到 set 中，可以重复添加，但不会有效果 
s.add(4)
s.add(4)
print(s)

# 通过 remove(key) 方法可以删除元素
s.remove(4)
print(s)

# set 可以看成数学意义上的无序和无重复的集合，因此，两个 set 可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 4, 5])
print('交集', s1 & s2)
print('并集', s1 | s2)

# set 和 dict 的唯一区别仅在于没有存储对应的value。但是，set 的原理和 dict 一样，所以，
# 同样不可以放入可变对象，# 因为无法判断两个可变对象是否相等，也就无法保证 set 内部‘不会有重复元素’。

s3 = set([1, 2, 3, (), 5, 6])
print(s3)

# 再议不可变对象
# 上面我们讲了，str 是不变对象， 而 list 是可变的对象
# 对于可变对象，比如 list ,对 list 进行操作，list 内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)

# 而对应不可变对象，比如 str,对 str 进行操作
a = 'abc'
print(a.replace('a', 'A'))

print(a)

# 虽然字符串有个 replace()方法，也确实变出了‘Abc’,但变量 a 最好仍是 ‘abc’,应该怎么理解呢
a = 'abc'
b = a.replace('a', 'A')
print('变量b:', b)
print('变量a:', a)

# 对于不变对象来说，调用对象自身的任意方法，也不会改变对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的


# 练习
# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
dict_2 = {'张三':'zhangsan'}
set_1 = set([3, 2, 1])
tup_1 = (1, 2, 3)
tup_2 = (1, [2, 3])
print(dict_2, set_1, tup_1, tup_2)

dict_2[tup_1] = '啥？'
print(dict_2)

# dict_2[tup_2] = '??'
# print(dict_2)
# TypeError: unhashable type: 'list'

print('old', set_1)
set_1.add(tup_1)
print('new', set_1)

# set_1.add(tup_2)
# print(set_1)
# TypeError: unhashable type: 'list'