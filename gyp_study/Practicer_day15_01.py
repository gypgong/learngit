# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
  # while s[0] == ' ':
    while s[:1] == ' ': # 每次切字符串首个元素判断是否为空格
        # s = s[1:len(s)] 指定开始位置和结束位置（注意左闭右开）
        s = s[1:] # 仅指定开始位置，切掉index为0的
  # while s[-1] == ' ':
    while s[-1:] == ' ': # 每次切字符串末尾元素判断是否为空格
        s = s[:-1] # 仅指定结束位置，切掉末尾元素（注意左闭右开）
    return s
    

''' 

# 思考为啥不能只能取字符串元素？（IndexError: string index out of range）
def trim(s):
    while s[0] == ' ':
        s = s[1:len(s)]        
    while s[-1] == ' ': 
        s = s[:-1] 
    return s 

'''

# **测试发现 对于一个空的数组或字符串，无任何元素，直接通过索引取值会报错，但通过切片方式则正常
# L = 'aa'

# L[:10]
# L[-10:]


# L[:1]
# L[-1:]

# L[0]
# L[-1]

# **官方解释
'''
The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. 
If i or j is greater than len(s), use len(s). If i is omitted or None, use 0. If j is omitted or None, 
use len(s). If i is greater than or equal to j, the slice is empty.

也就是说：

当左或右索引值大于序列的长度值时，就用长度值作为该索引值；

当左索引值缺省或者为 None 时，就用 0 作为左索引值；

当右索引值缺省或者为 None 时，就用序列长度值作为右索引值；

当左索引值大于等于右索引值时，切片结果为空对象。

'''






''' 

trim('a a a  ')


L = list(range(100))
print(L)
L[100:-1:1]


i = list(range(10-1,-1,-1))


print(i)
i[::-1]
i[-1:0]
i[1:(len(i)-1)]
i[1:-1]
i[1:]
i[0:1]
i[-1:0]
i[:-1]
i[0:-1]
# a = 'abc'
# print('a', len(a))

# b = ' '
# print('b', len(b))

# c = ''
# print('c', len(c))

# d = ' a '
# print('d', len(d)) 



trim('   aaaaa')
a = ' '
print(' '== a)

'''

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')