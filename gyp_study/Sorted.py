# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# **sorted()函数的基本语法格式如下
r = sorted(iterable, key=None, reverse=False)
''' 
iterable:表示知道的序列（可迭代对象）
key参数可以自定义排序规则
reverse参数指定以升序（False，默认）还是降序（True）进行排序
r：返回的是一个排好序的列表
注意：key参数和reverse参数是可选参数，即可以使用，也可以忽略
'''

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0].lower() # 开始没明白 这里抽象就是取L中tuple的首个元素

L2 = sorted(L, key=by_name)
print(L2)


# 再按照成绩从高到底排序：
def by_score(t):
    return -t[-1] # 转为负数映射 很有意思的思路
L2 = sorted(L, key=by_score)
print(L2)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 取L中每个元素的对应域(理解就是tuple的索引(index))
sorted(L, key=lambda L: L[0])
sorted(L, key=lambda L: -L[1])

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(students, key=lambda student : student[2])

