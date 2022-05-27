# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from types import MethodType

class Student(object):
    pass

def set_score(self, score):
    self.score = score

s = Student()
s2 = Student()

Student.set_score = set_score

s.set_score(100)
print(s.score)
print(s2.score)

