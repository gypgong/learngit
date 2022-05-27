# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用__slots__

class Stdudent(object):
    __slots__ = ('name', 'age')


s = Stdudent()
s.name = 'Michael'
s.age = 25
s.score = 99 # 由于‘score’没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# 使用__slots__要注意，__slots__定义的属性近对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Stdudent):
    pass

g = GraduateStudent()
g.score = 999

# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。



class Student(object):
    pass

# 给类绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score  # 这里是直接给Student的类，绑定类方法


# 给实例绑定方法
from types import MethodType

def set_score(self, score):
    self.score = score

s = Stdudent()

s.set_score = MethodType(set_score, s) # 注意区分，这里是利用MethodType方法给 实例s 绑定实例方法

