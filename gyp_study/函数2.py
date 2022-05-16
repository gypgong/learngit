# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# 给出坐标、位移、和角度，就可以计算出新的坐标：
def move (x, y, step, angle = 0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi /6)
print(x, y)


r = move(100, 100, 60, math.pi / 6)
print(r, type(r))


''' 
小结
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用 return 随时返回函数结果；
函数执行完毕也没有 return 语句时，自动 return None.
函数可以同时返回多个值，但其实就是一个tuple.
'''

''' 
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 
'''
def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    # elif not isinstance(b, (int, float)):
    #     raise TypeError('bad operand type')
    # elif not isinstance(c, (int, float)):
    #     raise TypeError('bad operand type')
    d = (b**2 - 4*a*c)
    if (a == 0 or d < 0):
        # 方程无解
        return -1
    elif d == 0:
        # 方程只有一个解
        x = x_1 = x_2 = (-b/(2*a))
        return x
    else:
        x_1 = ((-b + math.sqrt(b**2 - 4*a*c)) / (2*a))
        x_2 = ((-b - math.sqrt(b**2 - 4*a*c)) / (2*a))
        return x_1, x_2  


''' # 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
 '''

