# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ** 列表生成式
''' 
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
举例，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 可以用list(range(1, 11))
'''
list(range(1,11))

''' 
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一循环：
'''
L = []
for x in range(1, 11):
    L.append(x*x)

L

'''
但循环太繁琐，儿列表生成式则可以用一行语句代替循环生成上面的list:
'''
[x*x for x in range(1, 11)]

'''
写列表生产式时，要把生成的元素x*x放到前面，后面更for循环，就可以把list创建出来，十分有用，多谢几次，很快就可以熟悉这种语法。
for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
'''
[x*x for x in range(1, 11) if x % 2 == 0]

'''
还可以使用两层循环，可以生产全排列
'''
[m+n for m in 'abc' for n in 'ABC']

'''
三层和三层以上的循环就很少用到了
运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
'''
import os
[d for d in os.listdir('.')]




# **练习
''' 
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生产式会报错
使用内建的isinstance()函数可以拍断一个变量是不是字符串 
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [
    x.lower()  for x in L1  if isinstance(x, str)         
]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
