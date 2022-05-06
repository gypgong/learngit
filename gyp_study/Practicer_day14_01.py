# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 切片
# 取一个list或tuple的部分元素是非常常见的操作，比如，一个list如下：
L = ['Michael', 'Sarch', 'Tracy', 'Bob', 'Jack']

# 取前三个元素，应该怎么做？
#  笨办法
[L[0], L[1], L[2]]

# 取前N个元素，也就是索引为0-（N-1）的元素？可以用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

# i = 0
# while i <= n-1:
#     r.append(L[i])
#     i = i + 1

# print(r)

# 对于这种经常置顶索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
L[0:3] # 表示，从索引0开始取，知道索引3为止，但不包括索引3.即索引0，1，2，正好是3个元素。

L[:3] # 如果第一个索引是0，还可以省略

# 也可以从索引1开始取出2个元素
L[1:3]

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同意支持倒数切片，试试
L[-1:]
print(L)
L[-3:-1]



l = list(range(100))
print(l)
l[:10] # 取前10个
l[-10:] # 取后10个
l[10:20] # 取11-20个数

l[:10:2] # 前10个数中，每两个取一个

l[::5] # l列表中所有的数，每5个取一个

l[:] # 甚至什么都不写，只写[:]就可以原样复制一个list


# tuple也是一种list,唯一区别是tuple不可变。因此，tuple也可也用切片操作，只是操作的结果仍然是tuple
(0, 1, 2, 3, 4, 5)[:3]

# 字符串‘xxx’也可也看成是一种list，每个元素就是一个字符，因此，字符串也可也用切片操作，只是操作结果仍是字符串
'ABCDEFG'[:3]

'ABCDEFG'[:2]



# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    n = 0
    for i in s:
        if i != ' ':
            n = n + 1
            break
    s = s[n:(len[s]-1)]                   
    return  s


trim('   aaa')


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