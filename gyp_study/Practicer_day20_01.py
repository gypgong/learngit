# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    if s[0] != '-': # 正浮点数
        i = 0
        while s: # 循环找小数点的index
            if s[i] == '.':
                break
            i = i + 1  
        # i = s.index('.') # 找出'.'的index
        d = 10**(-(len(s) - i -1)) # 通过小数点index还原对应小数
        s = s[0:i] + s[i+1:] # s = [x for x in s if x != '.'] 列表生成式
    else: # 负浮点数
        s = s[1:] # 切掉'-'号（切片）
        i = 0
        while s: # 循环找小数点的index
            if s[i] == '.':
                break
            i = i + 1 
        # i = s.index('.')  # 找出'.'的index
        d = -(10**(-(len(s) - i -1))) # 通过小数点index还原对应小数，一并处理负数问题
        s = [x for x in s if x != '.']        
    def fn(x, y):
        return x * 10 + y
    def s2f(s):
        DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        return DIGITS[s]       
    return reduce(fn, map(s2f, s))*d

# 测试
print('str2float(\'-123.456\') =', str2float('-123.456'))
if abs(str2float('-123.456') - (-123.456)) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


