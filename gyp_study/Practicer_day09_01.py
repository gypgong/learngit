# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 增加默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 5))

print(power(5, 3))

''' 
设置默认参数的注意事项：
一是必选参数在前，默认参赛在后，否则Python的解释器会报错(个人思考：这里读取参数时，应该是从左到右，故不常用的放后面)
二是如何设置默认参数
当函数有多个参数时，把变化最大的参数放前面，变化小的参赛放后面。变化小的参数就可以作为默认参数

 '''

# 例如：我们写个一年级小学生注册函数，需要传入name 和 gender 两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

# 这样我们调用 enroll()函数只需要传入两个参数
enroll('Sarah', 'F')


print('==========分割线===========')

# 如果需要继续传入年龄、城市等信息？这样会使得函数的调用复杂度大大增加
# 可以把年龄和城市设置为默认参数
def enroll(name, gender, age=6, city = 'shenzhen'):

    print('name:', name),
    print('gender:', gender),
    print('age:', age),
    print('city:', city) 
    
enroll('Sarah', 'F')


enroll('Bob', 'M')

enroll('Adam', 'M', city = 'guangzhou')


print('==========分割线===========')
def	add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))

print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())
print(add_end())
''' 
定义默认参数要牢记一点：默认参数必选纸箱不变对象
'''


# 修改上面case,我们可以用 None这个不变对象来实现：
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())


