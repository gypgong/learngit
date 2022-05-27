# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from types import MethodType


class Student(object):
    def __init__(self, *args, **kw):
        self.name = kw.pop('name')
        self.age = kw.pop('age')
        self.score = kw.pop('score')


def set_score(self, value):
    self.score = value

def get_score(self, value):
    self.score = value
    return self.score


Student.set_score = MethodType(set_score, Student) # 这里写法有问题，MethodType的方法用于是给实例绑定方法，这里绑定给了类
Student.get_score = MethodType(get_score, Student)

t = Student(name = 'Bryan', age = 24, score = 80)
print(t.score)
print(dir(Student))
print(dir(t))
t.get_score(11)
t.set_score(100) # 思考为什么这里修改的是类属性，而不是实例属性
print(t.score)

print(Student.score)