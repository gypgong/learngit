# !/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
Python电脑猜
random库 randint的使用方式
random.randint(a,b) 生成一个[a,b]之间的整数 （包含a、b）
"""

''' 
import random

# 输入一个正确答案
answer = int(input('请输入答案：'))
# start表示范围开始值
start = 1
# end表示范围结束值
end = 100
# count依然用于统计次数
count = 0
# 电脑程序所猜第一个值，我们先在循环外得到
guess = random.randrange(start, end)
# 每循环一次，改变范围
while True:
    count += 1
    if guess > answer:
        print(f'电脑猜{guess}，猜大了')
        end = guess
        guess = random.randrange(start, guess)
    elif guess < answer:
        print(f'电脑猜{guess}，猜小了')
        start = guess + 1
        guess = random.randrange(start, end)
    else:
        print(f'正确答案：{answer}，电脑猜：{guess}：电脑猜了：{count}次猜中了')
        break 
'''




 
''' 
1、确认 猜数字区间1~99、1~999、1~9999
2、跟进区间默认输入第一个数字50、500、5000
3、跟提示大还是小，利用二分法循环计算最后下一个数字 
'''


''' def _fist_input(x):
    intlist = []
    if isinstance(x, int):
        if x == 50:
            intlist = list(range(1,100))
        elif x == 500:
            intlist = list(range(1,1000))
        elif x == 5000:
            intlist = list(range(1,10000))
        else:
            print('首次输入不是最优方案，防止最终猜数字次数过多请重新开始~!')
    return intlist
 '''

''' 
#  辅助猜数字demo
indexs = 1    
onelist = list(range(0,1000))
while True:
    nexts = 500        
    status = input('请输入状态,大了还是小了：')
    indexs += 1
    if status.lower() == 'x':
        onelist = onelist[(len(onelist)//2):]
        # print(onelist, len(onelist))
        nexts =onelist[len(onelist)//2]
        # print(nexts, onelist)
        # continue
        
    elif status.lower() == 'd':      
        
        onelist = onelist[0:(len(onelist)//2)]
        nexts =onelist[len(onelist)//2]
        # print(nexts, onelist)
        # continue

    elif status.lower() == 'c':
        print('That\'s it. You got it after ' +indexs+ 'tries')
        break
    print(nexts, onelist, indexs) 
'''





 

def main():
    ranges = range(1, 101)
    while True:
        num = input(u'请输入一个 1-100 的数字: > ')
        if not num.isdigit():
            continue
        times = 0
        while True:
            tags = input(u'你输入的数字是: > {}'.format(ranges[len(ranges)/2]))
            times += 1
            if tags.lower() == 'l':
                ranges = ranges[len(ranges)/2:]
                continue
            elif tags.lower() == 'h':
                ranges = ranges[:len(ranges)/2]
                continue
            elif tags.lower() == 'c':
                print(u'That\'s it. You got it after {} tries'.format(times))
                break
 
 
if __name__ == '__main__':
    main()
