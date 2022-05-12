# !/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 
# **可迭代对象（Iterable）
关于 Iterable，文档是这样定义的：

iterable
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an iter() method or with a getitem() method that implements Sequence semantics.

Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

提练重点如下：

1、它是能够一次返回一个成员的对象，也就是可以 for…in 遍历的；

2、所有的序列类型（也就是后面要说到的 Sequence），都是可迭代对象，如 list、str、tuple，还有映射类型 dict、文件对象等非序列类型也是可迭代对象；

3、自定义对象在实现了 iter() 方法或者实现了 getitem() 方法后，也可以成为可迭代对象；

4、iter()方法接受一个可迭代对象，该方法的返回值是一个迭代器（Iterator）

简单示例如下： 
'''
from collections import Iterable, Iterator
# 定义一个 list
l = [1, 2, 3]
print(isinstance(l, Iterable))  # True，列表是可迭代对象，同样 tuple、str、dict 也是的
 
# 遍历
for i in l:
    print(i)  # 每次遍历返回一个元素
 
# 自定义可迭代对象示例见下面注意事项
 
li = iter(l)
print(type(li))  # list_iterator
print(isinstance(li, Iterator))  # True
'''
那么如何判断一个对象是可迭代对象呢？很容易想到的方法是 isinstance，这时候我们需要注意一点，文档介绍如下：

class collections.abc.Iterable
ABC for classes that provide the iter() method.

Checking isinstance(obj, Iterable) detects classes that are registered as Iterable or that have an iter() method, but it does not detect classes that iterate with the getitem() method. The only reliable way to determine whether an object is iterable is to call iter(obj).

简单解释就是：
通过 isinstance(obj, Iterable) 判断一个对象是否是可迭代对象时，只有当这个对象被注册为 Iterable 或者当它实现了 iter() 方法的时候，才返回 True，而对于实现了 getitem() 方法的，返回的是 False。
所以稳当判断是否是可迭代对象的方式是调用 iter(obj)，如果不报错，说明是可迭代对象，反之则不是。

示例代码如下：
'''
"""
验证 Iterable
"""
# 导包
from collections import deque, Iterable, Iterator
 
# 定义一个啥都没有的类
class MyIterable1:
    pass
 
# 定义一个只实现了 __getitem__ 的类
class MyIterable2:
    def __init__(self, *args):
        self._list = deque()
        self._list.extend(args)
 
    def __getitem__(self, index):
        return self._list.popleft()
 
# 定义了一个只实现了 __iter__ 的类
class MyIterable3:
    def __init__(self, *args):
        self._list = deque()
        self._list.extend(args)
 
    def __iter__(self):
        return iter(self._list)
 
# mi = MyIterable1()
# iter(mi)  # 报错: TypeError: 'MyIterable1' object is not iterable
 
mi2 = MyIterable2(1, 2, 3)
# 可循环
for i in mi2:
    print(i)  # 1, 2, 3
print(isinstance(mi2, Iterable))  # False
iter(mi2)  # 不报错
 
mi3 = MyIterable3(1, 2, 3)
# 同样可遍历
for i in mi3:
    print(i)
iter(mi3)  # 同样不报错
print(isinstance(mi3, Iterable))  # 而这里返回是 True

'''
# **序列（Sequence）
关于 Sequence ，文档是这样定义的：

An iterable which supports efficient element access using integer indices via the getitem() special method and defines a len() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and bytes. Note that dict also supports getitem() and len(), but is considered a mapping rather than a sequence because the lookups use arbitrary immutable keys rather than integers.

The collections.abc.Sequence abstract base class defines a much richer interface that goes beyond just getitem() and len(), adding count(), index(), contains(), and reversed(). Types that implement this expanded interface can be registered explicitly using register().

提练重点如下：

1、可迭代；

2、支持下标访问，即实现了 getitem() 方法，同时定义了 len() 方法，可通过 len() 方法获取长度；

3、内置的序列类型：list、str、tuple、bytes；

4、dict 同样支持 getitem() 和 len()，但它不归属于序列类型，它是映射类型，因为它不能根据下标查找，只能根据 key 来查找；

5、抽象类 collections.abc.Sequence 还提供了很多方法，比如 count()、index()、contains()、reversed()可用于扩展；

总结结论：序列一定是一个可迭代对象，但可迭代对象不一定是序列。
'''  



'''
# **迭代器（Iterator）
上文档：

An object representing a stream of data. Repeated calls to the iterator’s next() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. Iterators are required to have an iter() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.

提练重点：

1、一个表示数据流的对象，可通过重复调用 next（或使用内置函数next()）方法来获取元素。当没有元素存在时，抛出 StopIteration 异常；

2、iter(obj)接受一个迭代器作为参数时，返回的是它本身。在可迭代对象里我们说过，iter(obj)方法不报错，说明它一定是一个可迭代对象。因此迭代器一定是一个可迭代对象；

3、一个迭代器必须要实现 iter() 方法。但因为迭代器前提必须是一个可迭代对象，所以只实现 iter() 方法不一定是一个迭代器。

示例代码如下：
'''
from collections import Iterable, Iterator, deque
 
 
print("="*30)
 
# 定义一个可迭代对象
l = [1, 2, 3]
 
# 转换成迭代器，只需要调用 iter(obj) 方法
li = iter(l)
print(isinstance(li, Iterator))  # True
 
# 可重复调用 next() 方法获取其中的一个元素
print(next(li))  # 1
print(next(li))  # 2
print(next(li))  # 3
 
# 每次获取完一个元素，这个元素就会被“消费”
# 当元素获取完毕后，报 StopIteration 异常
# next(li)  # StopIteration
 
 
print("=========iterator1=========")
# 当一个自定义类，只实现 __next__ 方法时
# 它不是一个可迭代对象，因此，它也不是一个迭代器
# 但是它可以调用 next() 方法获取值
class MyIterator1:
    def __init__(self, *args):
        self._list = deque()
        self._list.extend(args)
 
    def __next__(self):
        return self._list.popleft()
 
m1 = MyIterator1(1, 2, 3)
print(next(m1))
print(next(m1))
print(next(m1))
 
# print(next(m1))  # IndexError
print(isinstance(m1, Iterator))  # False
 
 
print("=========iterator2=========")
 
 
class MyIterator2:
    def __init__(self, *args):
        self._list = deque()
        self._list.extend(args)
 
    def __iter__(self):
        return iter(self._list)
 
    def __next__(self):
        return self._list.popleft()
 
 
m2 = MyIterator2(1, 2, 3)
print(next(m2))
print(next(m2))
print(next(m2))
 
# print(next(m2))  # IndexError
print(isinstance(m2, Iterator))  # True
 
 
print("=========iterator3=========")
 
 
class MyIterator3:
    def __init__(self, *args):
        self._list = deque()
        self._list.extend(args)
 
    def __getitem__(self):
        return iter(self._list)
 
    def __next__(self):
        return self._list.popleft()
 
 
m3 = MyIterator3(1, 2, 3)
print(next(m3))
print(next(m3))
print(next(m3))
 
# print(next(m3))  # IndexError
print(isinstance(m3, Iterator))  # False

'''
总结结论：

1、迭代器一定是可迭代对象，但可迭代对象不一定是迭代器；

2、可迭代对象可以通过直接调用 iter(obj) 方法转换成迭代器；

3、自定义对象转换迭代器，必须实现 iter 和 next 。同时实现 getitem 和 next 也是可以达到 next() 访问值的效果，但是通过 isinstance 判断返回 False，这里返回 False，应该和可迭代器判断返回 False 的原因是一致的；

4、迭代器每次调用 next() 能拿到一下值，但它是一次性消费的，当获取使用过后，无法再拿到原来的值。
'''


''' 



# **生成器（generator）
文档解释如下：

A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

提练重点：

1、它是一个迭代器；

2、它是一个含有特殊关键字 yield 的迭代器；

3、每次生成一个值，可通过 next() 方法获取。

实际上生成器的实现有两种方式，一种是通过 yield 关键字，另外一种是通过生成器表达式，示例代码如下：
'''
import types
 
# yield 方式
def my_generator():
    for i in range(3):
        yield i
 
g = my_generator()
print(type(g))  # <class 'generator'>
isinstance(g, types.GeneratorType)  # True
next(g)  # 0
next(g)  # 1
next(g)  # 2
next(g)  # exception StopIteration
 
# 使用生成器表达式
l = [i for i in range(3)]  # 列表推导式
g = (i for i in range(3))  # 将 [] 换成 () 即是生成器表达式
isinstance(g, types.GeneratorType)  # True

''' 
总结
1、迭代的方式有两种，一种是通过下标，即实现 getitem，一种是直接获取值，即实现 iter，两种方式都可通过 for…in 方式进行遍历。也都是可迭代对象；

2、isinstance 判断可迭代对象时，针对下标访问的判断有出入，需要特别注意；

3、可迭代对象基本要求是可遍历获取值；

4、序列一定是可迭代对象，它实现了 len() 和 getitem，可获取长度，可通过下标访问；

5、迭代器一定是可迭代对象，它实现了 next()；

6、生成器是特殊的迭代器，它一定是迭代器，因此也一定是可迭代对象。
'''