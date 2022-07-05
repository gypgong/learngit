# !/usr/bin/env python3
# -*- coding: utf-8 -*-





import multiprocessing
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('我是子进程(%s),我的父进程是(%s).' % (os.getpid(), os.getppid()))
else:
    print('我(%s)刚刚创建了一个子进程(%s).'% (os.getpid(), pid))





# multiprocessing

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('运行子进程 %s(%s)' % (name, os.getpid()))

if __name__=='__main__':
    print('父进程 %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程将启动')
    p.start()
    p.join()
    print('子进程结束') 





# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.(%s)' % (name, (end - start), os.getpid()))

if __name__=='__main__':
    print('Process process %s.' % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Warning for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


 
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

"""  """

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b' set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)





