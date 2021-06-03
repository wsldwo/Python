# 多进程
# 父进程与子进程
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
from multiprocessing import Process,Pool
import os,time,random
def proc1_run(): #打印10以内奇数
    start = time.time()
    x = 1
    while x < 10 :
        print('Child pid: #%s print: %s' % (os.getpid(),x))
        time.sleep(random.random())
        x += 2
    end = time.time()
    print('Child pid: #%s runs %s seconds' % (os.getpid(),(end - start)))
def proc2_run(): #打印10以内偶数
    start = time.time()
    x = 2
    while x < 10 :
        print('Child pid: #%s print: %s' % (os.getpid(),x))
        time.sleep(random.random())
        x += 2
    end = time.time()
    print('Child pid: #%s runs %s seconds' % (os.getpid(),(end - start)))



# 多线程
# 主线程与子线程
import threading
bablance = 1000 # 初始余额
# 取钱
def withdraw():
    global bablance
    for x in range(10):
        value = random.randint(1,1000)
        if bablance >= value:
            bablance -= value
            print('取钱：%s,余额：%s' % (value,bablance))
        else:
            print('取钱：%s,操作失败，余额不足！' % value)
# 存钱
def deposit():
    global bablance
    for x in range(10):
        value = random.randint(1,1000)
        bablance += value
        print('存钱：%s,余额：%s' % (value,bablance))
t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=deposit)

# Lock
# 多线程中，所有变量都由所有线程共享
lock = threading.Lock()

# 核心操作部分
lock.acquire()
try:
    pass #安全操作
finally:
    lock.release()



if __name__ == '__main__': #有点像C、Java中的Main方法
    print('Parent pid: %s' % os.getpid())
    p1 = Process(target=proc1_run)
    p2 = Process(target=proc2_run)
    p1.start()
    p2.start()
    p1.join() #等待p1执行完
    p2.join() #等待p2执行完
    t1.start()
    t2.start()