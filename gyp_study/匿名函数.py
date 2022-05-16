# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# **匿名函数
'''
Python使用lambda来创建匿名函数
所谓匿名，意即不再使用def语句这样标准的形式定义一个函数。
    
    lambda只是一个表达式，函数体比def简单很多
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率


语法
lambda函数的语法只包含一个语句，如下：
lambda[arg1[,arg2,...agrn]]:expression


'''


# 练习
# 请用匿名函数改造下面代码：
def is_odd(n):
    return n % 2 ==1

L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 ==1 , range(1, 20)))
print(L)
