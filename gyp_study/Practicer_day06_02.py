# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义函数
''' 在Python中,定义一个函数要使用 def 语句,依次写出函数名、括号、括号中的参数和冒号：,然后,在缩进模块中编写函数体,函数的返回值用return语句返回
我们以自定义一个求绝对值的my_abs函数为例 '''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs(-5), my_abs(6))

# 如果想定义一个什么事也不做的空函数，可以用 pass 语句
def nop():
    pass

# pass 语句什么都不做，哪有什么用 实际上 pass 可以用来作为占位符，比如现在还没想好 怎么写函数的代码，就可以先放一个 pass ,让代码能运行起来
# pass 还可以用在其它语句里，比如
''' if age >= 18:
    pass '''

# 缺少pass，代码运行就会有语法错误

# 参数检查
# 调用函数时，如果参赛个数不对，Python 解释器就会自动检查出来，并抛出 typeError
# print(my_abs('a'))

# print(abs('a'))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs('a'))

