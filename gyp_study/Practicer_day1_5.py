#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 'ABC'
b = '中文'
c = 58619919

print(a.encode('ascii'))
print(b.encode('utf-8'))
#print(c.encode('utf-8'))
#print(b.encode('ascii'))

a = a.encode('ascii')
b = b.encode("utf-8")
#c = c.encode('utf-8')

print(a.decode('ascii'))
print(b.decode('utf-8'))
#print(c.decode('utf-8'))
