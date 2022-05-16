# -*- coding: utf-8 -*-

def area_of_circle(r):
    pi = 3.1415926535654
    if r <= 0:
        return None
    else:
        S = pi*r**2
        return S


# s1 = s1.area_of_circle(r)
print(area_of_circle(2.5))

print(help(abs))

print(abs(100), abs(-20), abs(12.34))


# print(abs(1, 2))   TypeError: abs() takes exactly one argument (2 given)

# print(abs('a'))    TypeError: bad operand type for abs(): 'str'

print(help(max))

print(max(1, 2, 3), max(2, 3, 4, 5, -6))


# 数据类型转换
# 字符串类型转换为整型
print('123', type('123'))
print(int('123'), type(int('123')))

# 字符串类型转换为浮点型
print('12.34', type('12.34'))
print(float('12.34'), type(float('12.34')))

# 浮点型类型转换为字符串
print(1.5, type(1.5))
print(str(1.5), type(str(1.5)))

# 整型类型转换为字符型
print(100, type(100))
print(str(100), type(str(100)))


# 整型类型转换为布尔型
print(1, type(1))
print(bool(1), type(bool(1)))

# 字符型类型转换为布尔型
print('', type(''))
print(bool(''), type(bool('')))

# 函数名其实就是指向一个函数对象的引用，完全可以把一个函数名赋给一个变量，相当于给函数起了一个‘别名’
a = abs
print(a(-20))
print(help(a))

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
print(help(hex))
n1 = 255
n2 = 1000
print
(hex(255), type(hex(255)),
 hex(1000), type(hex(1000)))



