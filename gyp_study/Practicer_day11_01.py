# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def mul(*args):
    if len(args)==0:
        raise TypeError('bad operand type args\'s TypeError')
    else:
        args_num = 1
        for n in args:
            if not (isinstance(n, (int, float))):
                raise TypeError('bad operand type args\'s TypeError')
            else:
                args_num = args_num * n
        return args_num



# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')