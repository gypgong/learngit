# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ** 生成器
'''
通过列表生成式，我们可以直接创建一个列表。但是，受内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅会占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所有，如果列表元素跨页按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list,从而节省大量的空间，在Python中，
这种一遍循环一边计算的机制，称为生成器：generator.

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改为(),就创建了一个generator:
'''
L = [x*x for x in range(10)]
print(L)

g = (x*x for x in range(10))
print(g)

'''  
创建L和g的区别仅在于最外层[]和()，L是一个list，而g是一个generator.
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
'''

g = (x*x for x in range(10))
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g) # Traceback (most recent call last):  File "<stdin>", line 1, in <module> StopIteration (超出会抛出异常)

'''
我们讲过，generator保存的是算法，每次调用next(g),就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，
抛出StopIteration的错误。
当然，上面这种不断调用next(g) 实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
'''
g = (x*x for x in range(10))

for n in g:
    print(n)


'''
所以，我们创建一个generator后，基本上永远不会调用next(),而是通过for循环来迭代它，并且不需要关系StopIteration的错误。
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二数外，任意一个数都可以由前面两个数相加得到：
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b 
        # 注意赋值语句 a, b = b, a+b 
        # 相当于 t = (a, a+b), t是一个tuple, 
        # a = t[0]
        # b = t[1]
        # 但不比显式写出临时变量t就可以赋值
        n = n + 1
    return 'done'


'''
上面的函数可以输入斐波那契数列的前N个数：

'''
fib(10)

'''
仔细观察，就可以看出，fib函数实际上是定义了斐波那契数列的推送规则，可以从第一元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator.
也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator函数，只需要吧print(b)改为yield b就可以了
'''
def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

'''  
这种定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用
一个generator函数将返回一个generator：
'''
f = fib(6)
print(f)

'''
这里，最难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到return语句或最后一行函数语句就返回。而变成generator的函数，在每次调用
next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

举个简单例子，定义一个generator函数，依次返回1，3，5
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

''' 
调用该generator函数时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
'''
o = odd()

next(o)
next(o)
next(o)
next(o)

'''
可以看到，odd 不是普通函数，而是generator函数，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)
就报错
'''
# **请务必注意：调用generator函数会创建一个generator的对象，多次调用generator函数会创建多个相互独立的generator.

'''
证明case 这样调用next()每次都返回1
'''
next(odd())
next(odd())
next(odd())
next(odd())
'''
原因在于odd()会创建一个新的generator对象，上述代码实际上创建了3个完全独立的generator，对3个generator分别调用next()当然每个都会返回第一个值。
正确的写法是创建一个generator对象，然后不断对这一个generator对象调用next()
'''
g = odd()
next(g)
next(g)
next(g)
'''
回到fib的例子，我们在循环的过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产品一个无限数列出来。
同样的，把函数改成generator函数后，我们基本上从来不会next()来获取下一个返回值，而是直接使用for循环来迭代：
'''
def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
''' 
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
'''
g = fib(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value', e.value)
        break
        
# def triangles():
#     L = [1]
#     while True:   
#         yield  L    
#         medium = [0] +L+ [0]    
#         L = [medium[i] + medium[i+1] for i in range(len(L)+1)]


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]



L = [1, 2, 1]
[L[n] + L[n + 1] for n in range(2)]

medium = [0] +[1, 2, 1]+ [0]
print(medium)

list1 = list(range(0))
list2 = list(range(1))
print(list1, list2)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')