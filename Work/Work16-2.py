#TCP协议编程
#服务器
import socket,threading,time

# 连接处理函数
def sockHandle(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    while True:
        # 接收数据
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        print('recv data:%s' % data.decode('utf-8'))
        # 发送数据
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    # 关闭连接
    sock.close()
    print('Connection from %s:%s closed!' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET指定使用IPv4协议,SOCK_STREAM指定使用面向流的TCP协议
# 监听端口
s.bind(('127.0.0.1',3806))
# 指定等待连接的最大数量
s.listen(4)
while True:
    # 接受一个新连接:
    sock,addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=sockHandle,args=(sock,addr))
    t.start()
    print('#######@@@@@$$$$$$')

    break # 防止程序无法退出

