# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ** filter()（过滤器）

''' 
filter()函数用于 过滤 可迭代对象中不符合条件的元素，返回由符合条件的元素组成的新的迭代器。
filter()函数把传入的函数依次作用于每个元素，然后根据返回值是True还是False，来巨大保留或丢弃该元素。

r = filter(function, iterable)
function：用于实现判断的函数，可以为 None。
iterable：可迭代对象，如列表、range 对象等。
返回值r：返回一个
'''

# 练习
# 回数是指从左向右读和从右从左读都是一样的数，隶属12321，909.请利用filter()筛选出回数。
def is_palindrome(n):
    if isinstance(n, int): # n是否int
        return n == int(str(n)[::-1]) # 转为str 切片反转序列输出


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')