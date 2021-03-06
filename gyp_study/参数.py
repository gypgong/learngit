# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# **位置参数
# 计算x二次方的函数
def power(x):
    return x * x
print(power(5))


# 计算任意n次方：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 5))



# **增加默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 5))

print(power(5, 3))

''' 
设置默认参数的注意事项：
一是必选参数在前，默认参赛在后，否则Python的解释器会报错(个人思考：这里读取参数时，应该是从左到右，故不常用的放后面)
二是如何设置默认参数
当函数有多个参数时，把变化最大的参数放前面，变化小的参赛放后面。变化小的参数就可以作为默认参数

 '''

# 例如：我们写个一年级小学生注册函数，需要传入name 和 gender 两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

# 这样我们调用 enroll()函数只需要传入两个参数
enroll('Sarah', 'F')


print('==========分割线===========')

# 如果需要继续传入年龄、城市等信息？这样会使得函数的调用复杂度大大增加
# 可以把年龄和城市设置为默认参数
def enroll(name, gender, age=6, city = 'shenzhen'):

    print('name:', name),
    print('gender:', gender),
    print('age:', age),
    print('city:', city) 
    
enroll('Sarah', 'F')


enroll('Bob', 'M')

enroll('Adam', 'M', city = 'guangzhou')


print('==========分割线===========')
def	add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))

print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())
print(add_end())
''' 
定义默认参数要牢记一点：默认参数必选纸箱不变对象
'''


# 修改上面case,我们可以用 None这个不变对象来实现：
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())



# **可变参数
''' 
以数学题为例，给定一组数字a, b, c ......,请计算所有数字的平方之和
要定义出这个函数，我们必选确定输入的参数。由于参数个数不确定，我们首先想到可以把a, b, c ......作为一个list或tuple传进来，这样函数可以定义如下：
 '''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum +n*n
    return sum

# 但是调用的时候，需要先组装出一个list 或 tuple
calc([1, 2, 3])

calc([1, 3, 5, 7])

# 如果利用可变参数，调用函数的方式可以简化成这样：
# calc(1, 2, 3)

# calc(1, 3, 5, 7)


# 所以需要把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

calc(1, 2, 3)

calc(1, 3, 5, 7)


''' 
定义可变参数和定义一个list 或 tuple参数相比，仅仅在参数前面加了一个 * 号。
在函数内部，参数 numbers 接收到的是一个 tuple 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
'''

calc()

calc(1, 3)

# 如果已经有一个list 或者 tuple,要调用一个可变参数怎么办？可以这样做
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])

# 写法是可行的，但太繁琐，所以Python允许你在list 或tuple 前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]

calc(*nums)
#  *nums 表示把 nums 这个list的所有元素作为可变参数穿进去。这种写法想当有用，而且很常见




# **关键字参数

''' 
可变参数允许你传入0个 或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数都在函数内部自动组装为一个dict。 看例子：
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#  函数person 除了必选参数 name和 age外，还接受关键字参数kw，在调用该函数时，可以只传入必选参数

person('Michael', 30)

extra = {'city': 'shenzhen', 'job': 'Engineer'}
person('Jack', 26, city = extra['city'], job = extra['job'])
# 上面负责的调用可以用简化的写法
extra = {'city': 'shenzhen', 'job': 'Engineer'}
person('Jack', 26, **extra)
''' 
**extra 表示把 extra 这个dict的所有key-value用关键字参数传入到函数的 **kw参数， kw将获得一个dict,
注意 kw获得的dict 是extra 的一份拷贝，对kw 的改动不会影响到函数外的extra
'''



#  **命名关键字参数

''' 
对应关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了那些，就需要在函数内部通过 kw检查
仍以person()函数为例，我们希望检查是否有city 和job 参数。 
'''
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 但是调用者仍可以传入不受限制的关键字参数：
person('Jack', 26, city='shenzhen', addr='nanshan', zipcode=888888)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，直接收city 和job 作为关键字参数。这种定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符 * ，* 后面的参数被视为命名关键参数。
# 调用方式如下：
person('Jack', 26, city='shenzhen', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 * 了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必需传入参数名，这和位置数不同，如果没有传入参数名，调用将会报错；
person('Jack', 26, 'shenzhen','Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'

# 由于调用时缺少参数名city 和job ,Python解释器把前两个参数视为位置参数，后两个参数传给 *args , 但缺少命名字参数导致报错
# 命名关键字参数可以有缺省值（以为可以让某个参数带有默认值，每次传参时可省略），从而简化调用
def person(name, age, *, city = 'shenzhen', job):
    print(name, age, city, job)

# 由于命名关键字参数city 具有默认值，调用时，可不传入city 参数
person('Jack', 26, job='Engineer')


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为分隔符。如果缺少 * ，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 * ，city 和job 被视为位置参数
    pass


# **参数组合

''' 
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，但是请注意，参数定义的顺序必须是：
必选参数、默认参数、可变参数、命名关键字参数和关键字参数
'''
# 比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
    pass

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
    pass

# 在调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1, 2)

f1(1, 2, c=5)

f1(1, 2, 3,'a', 'b')

f1(1, 2, 3,'a', 'b', x=99)


f2(1, 2, d=99, ext=None)


# 最神奇的是通过一个tuple 和dict， 你也可以调用上述函数
args = (1, 2, 3, 4)

kw = {'d': 99, 'x': '#'}

f1(*args, **kw)


args = (1, 2, 3)

kw = {'d': 88, 'x': '#', 'f': 66}

f2(*args, **kw)

# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
''' 
虽然可以组合多大5种参数，但不要同时使用太多的组合，否则函数的接口可理解性很差
'''

# 练习
# 以下函数允许计算两个数的乘机，请稍加改造，变成可接收一个或多个数并计算乘积

# def mul(x, y):
#     return x * y

def mul(*args):
    if len(args)==0:
        raise TypeError('bad operand type args\'s TypeError')
    else:
        args_num = 1
        for n in args:
            if not (isinstance(n, (int, float))):
                raise TypeError('bad operand type args\'s TypeError')
            else:
                args_num = args_num * n
        return args_num



# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


