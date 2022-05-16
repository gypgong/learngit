# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# ** 闭包函数
'''
如果在一个函数的内部定义了另一个函数，外部的我们叫他外函数，内部的我们叫他内函数。

闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包

一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量消失。但闭包是一种特殊情况，如果外函数在结束的时候
发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。
'''

# **返回闭包是牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# **使用闭包时，对外层变量赋值前，需要先使用nonlocal声明改变量不是当前函数的局部变量。

# 练习
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x 
    return counter



# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')