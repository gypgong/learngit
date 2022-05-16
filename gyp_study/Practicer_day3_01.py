# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# list栏目的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))


# tuple
# 另一种有序列表叫元组：tuple.tuple和list非常类似，单tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Miachael', 'Bob', 'Tracy')

print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
# print(classmates[-4])

t = (1, 2)
print(t)

# 定义一个空的tuple
t = ()
print(t)

# 定义一个只有1个元素的tuple,易错点
''' 定义的不是tuple,是 1 这个数 这是因为括号()既可以表示tuple,又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算的结果自然是 1  ''' 
t = (1)   
print(t)

# 所以，只有一个元素的tuple定义时，必需加一个逗号 , ，来消除歧义：
t = (1,)
print(t)

# "可变的"tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple
print(L[0][0])

# 打印Python
print(L[1][1])

# 打印Lisa
print(L[2][2])


print('=================分割线==============')

''' 根据Python的缩进规则,若果if语句判断是True, 就把缩进的两行print语句执行了,否则，什么也不做'''
age = 20
if age >= 18:
    print('you age is', age)
    print('adult')

''' 也可也给if添加一个else语句,意思是,如果id判断是False,不要知悉if的内容,去吧else的执行了 '''
age = 3
if age >= 18: # 注意不要少写了冒号 :
    print('your age is', age)
    print('adult')
else: # 注意不要少写了冒号 :
    print('your age is', age)
    print('teenager')


''' 上面的判断，也可以用elif更加细致判断 '''
age = 3
if      age >= 18:
    print('adult')
elif    age >= 6:
    print('teenager') 
else:
    print('kid')

''' 

elif是else if的缩写,完全可以有多个elif,所以if语句的完整形式如下 
if 《条件判断1》:
    <执行1>
elif《条件判断2》:
    <执行2>
elif《条件判断3》:
    <执行3>
else:
    <执行4>

'''

'''
if语句有个特点,它是从上往下判断，如果在某个判断上是True,把该判断对应的语句执行后,忽略掉剩下的elif和else 
'''
age = 20 
if      age >= 6:
    print('teenager')
elif    age >= 18:
    print('adult')
else:
    print('kid')

''' 
#  if判断条件还可以简写
if x: # 只要 x 是非零数值,非空字符串,非空list等,就判断为True,否则为False
    print('True') 
'''

# input() 返回的数据类型是str
# birth = int(input('birth'))
# birth = input('birth:') 
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# TypeError: '<' not supported between instances of 'str' and 'int'

# 修改下
# birth = int(input('birth:'))
# # birth = input('birth:') 
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# # ValueError: invalid literal for int() with base 10: 'abc' 输入abc 会报错


''' 
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果： 
'''
height = float(input('请输入身高(m):'))
weight = float(input('请输入体重(kg):'))
temp = float(weight/(height**2))
print('temp = ', temp)
print(type(temp))
bmi = float('%.1f' % temp)
print(bmi)
if              bmi < 18.5:
    print('bmi指数为:', bmi ,'过轻,不要挑食哦，注意营业均衡,小明')
elif    18.5 <= bmi < 25:
    print('bmi指数为:', bmi ,'正常,继续保持,小明')
elif    25   <= bmi < 28:
    print('bmi指数为:', bmi ,'过重,要控制碳水和脂肪的摄入哦和加强运动,小明')
elif    28   <= bmi < 32:
    print('bmi指数为:', bmi ,'肥胖,必要控制碳水和脂肪的摄入哦和加强运动,小明')
else:	
    print('bmi指数为:', bmi ,'严重肥胖,一定要控制碳水和脂肪的摄入哦和加强运动,小明')








