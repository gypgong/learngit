# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印表单名称
print("武侠居中层领导列表")

# 设定一个模版
template = '序号:%04d\t 姓名:%s \t性别:%s \t年龄:%d岁 \t部门:武侠局-%s科长'

# 逐条设定要往模版中填充的内容
information_1 = (1,'张三丰','男',150,'大保健')
information_2 = (2,'张无忌','男',22,'行动组')
information_3 = (3,'沈万三','男',55,'后勤组')
information_4 = (4,'郭靖','男',45,'保卫科')
information_5 = (5,'瑛姑','女',60,'财务科')
information_6 = (6,'黄蓉','女',40,'情报科')
information_7 = (7,'杨过','男',36,'战斗组')

print(template%information_1)
print(template%information_2)
print(template%information_3)
print(template%information_4)
print(template%information_5)
print(template%information_6)
print(template%information_7)

print('----------------华丽分割线--------------')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


print('================华丽分割线==============')

print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' %7) #后面两个%%表示一个%，多一个表示转义

# format()
print('Hello, {0}, 成绩提升了 {1:.2f}%'. format('小明', 17.125))

# f-string 
r = 2.5
s = 3.14 * r ** 2 
print(f'The area of circle with radius {r} is {s:.2f}')


s1 = 72
s2 = 85
increase = float((s2 - s1) / s2)
print(f'Hello, 你去年的成绩{s1}, 今年的成绩{s2},' '成绩提升了%.2f %%' % increase) 



print('中文'.encode('gb2312'))


print('================华丽分割线==============')
#list 和 tuple
classmates = ['Michael','Bob','Tracy']
print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
#print(classmates[3]) 索引越界 IndexError：list index out of range
# 最后一个元素的索引是-1

print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

print('================华丽分割线==============')
classmates = ['Michael','Bob','Tracy']
print(classmates)

# 往list中追加元素待末尾 append(objec)
classmates.append('Adam')
print(classmates)

# 把元素插入到指定位置，比如索引为 1 的位置 insert(index,objec)
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(index)方法，index是索引位置
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)



