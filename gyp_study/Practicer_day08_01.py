# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算x二次方的函数
def power(x):
    return x * x
print(power(5))


# 计算任意n次方：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 5))






