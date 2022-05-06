# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 练习
# 请使用迭代查找一个list中最小和最大的值

def findMinAndMax(L):
    if L:
        max = L[0]
        min = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
    #    min = max = None       
    # elif len(L) == 1:
    #    min = max = L[0]
    else:
        min = max = None 
        # max = L[0]
        # min = L[0]
        # for i in L:
        #     if i < min:
        #         min = i
        #     if i > max:
        #         max = i
    return (min, max) 



# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')