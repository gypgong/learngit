# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 遍历的方式，不能支持index 会报错 见下面case
s = '152.02'
i=0
# for s[i] in s:
#     if s[i] == '.':
#         break
#     i = i + 1
# print(i)  # TypeError: 'str' object does not support item assignment


while s:
    if s[i] == '.':
        break
    i = i + 1
print(i)

