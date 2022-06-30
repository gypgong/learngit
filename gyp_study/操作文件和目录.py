# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 本节禁止运行或调试

# 操作文件和目录

import os

os.name # 操作系统类型（‘posix’说明是Linux、unix、Mac os x，如果是nt，就是windows）

os.uname() # 获取详细的系统信息

# 环境变量
os.environ # 查看环境变量

os.environ.get('PATH') # 获取path环境变量的值

os.environ.get('x', 'default')

# 操作文件和目录

# 查看当前目录的决定路径：
os.path.abspath('.')
'/Users/gypgong/Documents/learngit/gyp_study'

# 在某个目录下创建一个新的目录。首先把新的目录的完整路径表示出来：
os.path.join('/Users/gypgong/Documents/learngit/gyp_study', 'testdir')

# 然后创建一个目录：
os.mkdir('/Users/gypgong/Documents/learngit/gyp_study/testdir')

# 删掉一个目录：
os.rmdir('/Users/gypgong/Documents/learngit/gyp_study/testdir')


# 把两个路径合成一个时，不要直接拼接，而是要通过os.path.join()函数，可以正确处理不同操作系统的路径分隔符
os.path.join('/Users/gypgong/Documents/learngit/gyp_study', 'testdir')

# 同理，要拆分路径时，也不要直接去拆字符串，而是要通过os.path.split()函数，可以把一个路径拆分成为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/Users/gypgong/Documents/learngit/gyp_study/testdir/file.txt')

# 合并、拆分路径的函数并不要求目录和文件要真实存在，他们只对字符串进行操作


# 文件操作使用下面函数.假定当前目录下存在一个test.txt文件

os.rename('test.txt', 'test') # 对文件重命名

os.remove('test.py') # 删掉文件

[x for x in os.listdir('.') if os.path.isdir(x)] # 列出当前目录下的所有目录

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] # 列出所有.py文件





import os
def outputDir(dir, a):
    if os.path.isdir(dir):
        d = os.listdir(dir)
    for f in d:
        a.append(f)
        outputDir(os.path.join(dir, f), a)
              

a = []
outputDir('.', a)
print(a)


print('================分割线===============')

import os
def outputDir(dir, a, p):
    if os.path.isdir(dir):
        d = os.listdir(dir)
        for f in d:
            path = os.path.join(dir, f)
            a.append(f)
            p.append(path)
            outputDir(path, a, p)

a = []
p = []
outputDir('./.vscode', a, p)
for n, x in enumerate(a):
    if x.find('main') != -1:
        print(p[n])