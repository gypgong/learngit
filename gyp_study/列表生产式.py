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

'''
for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
'''
d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k,'=', v)

'''
因此，列表生成式也可以使用两个变量来生成list：
'''
d = {'x':'A', 'y':'B', 'z':'C'}
[k + '='+ v for k,v in d.items()]

'''
最后把一个list中所有的字符串变成小写：
'''
L = ['Hello', 'Wrold', 'IBM', 'Apple']
[s.lower() for s in L]

# **if ... else
'''
使用列表生成式的时候，有些童鞋经常搞不清if ... else的用法。
例如，以下代码正常输出偶数：
'''
[x for x in range(1, 11) if x%2 == 0]

'''
但是，我们不能在最后的if加上else：
'''
# [x for x in range(1,11) if x%2 == 0 else 0] 语法错误 SyntaxError: invalid syntax

''' 
这是因为for后面的if是一个筛选条件，不能带else，否则如何筛选？
另外有同学发现把if写在for前面必须加else，否则会报错：
'''
# [x if x%2 == 0 for x in range(1,11)] 语法错误 SyntaxError: invalid syntax


'''
这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。因此考察表达式：x%2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else:
'''
[x if x%2 == 0 else -x for x in range(1, 11)]

'''
上述for前面的表达式x if x%2 ==0 else -x 才能根据x 计算出确定的结果
可见，在一个列表生成式中，for前面的if...else是表达式，而for后面的if是过滤条件，不能带else。
'''



# **练习
''' 
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生产式会报错
使用内建的isinstance()函数可以拍断一个变量是不是字符串 
'''
#  L = ['Hello', 'World', 18, 'Apple', None]   属性错误ttributeError: 'int' object has no attribute 'lower'
# [s.lower() for s in L]


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
