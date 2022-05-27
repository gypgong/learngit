# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意：属性的方法名不要和实例变量重名，例如，以下的代码是错误的
class Student(object):

    # 方法名称和实例变量均为birth
    @property
    def birth(self):
        return self.birth

# 这是因为调用s.brith时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错 RecursionError


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    
    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, value):
        self.w = value


    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, value):
        self.h = value


    @property
    def resolution(self):
        return self.w * self.h

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')