# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# type()

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)

h = Hello()
h.hello()


print(type(Hello))

print(type(h))


print('============分割线===========')

def fn(self, name='world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
h.hello()

print(type(Hello))

print(type(h))

""" 
要创建一个class对象，type()函数依次传入3个参数：
1.class的名称
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类。别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""



# metaclass

