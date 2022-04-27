# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#  for x in ... 循环就是把每个元素带入变量x，然后执行缩进块的语句

# 比如想计算1-10的整数之和，可以用一个 sum 变量做累加：
sum = 0
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in L:
    sum = sum + x
print(sum)

# 如果要计算1-100的和，从1写到100有些困难，幸好Python提供一个range()函数，
# 可以生产一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
list_1 = list(range(5))
print(list_1)

# 计算1-100的整数之和
sum = 0 
for x in range(101):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum =0 
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)

# break 
# 在循环中， break 语句可以提前退出循环，例如，本来要循环打印1-100的数字：
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# 如果要提前结束循环，可以用 break 语句：
n = 1 
while n <= 100:
    if n > 10: # 当 n = 11 时，会执行 break 语句
        break #break语句会结束当前循环
    print(n)
    n= n + 1
print('END')
# 执行上面的代码可以看到，打印1-10后，紧接着打印END,程序结束。 可见 break 的作用是提前接受循环。


print('========分割线========')
# continue
# 在循环的过程中，也可也通过 continue 语句，跳过当前的这次循环，直接开始下一次循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print('END')



# 死循环
''' n = 1
while n > 0:
    n = n+1           
    print(n)
print('END---') '''

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
i = 0
while i <= len(L)-1:
    print('hello', L[i], '!')
    i = i + 1

for name in L:
    print('hello', name, '!')

for name in L:
    print('hello %s !' % name)

