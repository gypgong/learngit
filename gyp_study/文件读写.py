# !/usr/bin/env python3
# -*- coding: utf-8 -*-

fpath = './IOtest.txt' # fpath = '/Users/gypgong/Documents/learngit/gyp_study/IOtest.txt'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(fpath, 'w') as f:
    f.write('hello, world~!')

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(fpath, 'a') as f:
    f.write('\nAdd one line.')

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
    
