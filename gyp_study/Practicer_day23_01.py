# !/usr/bin/env python3
# -*- coding: utf-8 -*-

#  去点字符串首尾空格
name = input()
# print(name.strip())
def trim(name):
    while name[:1] == ' ' or name[:1] == '\t':
        name = name[1:]
    while name [-1:] == ' ' or name[-1:] == '\t':
        name = name[:-1]
    return name
s = trim(name)
print(s)