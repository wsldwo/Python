# 协程，一种单线程模型
# async await
# 在一个coroutine的耗时操作期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
# 如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行
import asyncio

async def work1():
    print('#work1 start:')
    await asyncio.sleep(2) # asyncio.sleep()也是一个coroutine，模拟耗时操作2s
    print('#work1 finished!')
async def work2():
    print('#work2 start:')
    await asyncio.sleep(2) # asyncio.sleep()也是一个coroutine，模拟耗时操作2s
    print('#work2 finished!')
async def work3():
    print('#work3 start:')
    await asyncio.sleep(2) # asyncio.sleep()也是一个coroutine，模拟耗时操作2s
    print('#work3 finished!')

loop = asyncio.get_event_loop()
tasks = [work1(),work2(),work3()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


