#TCP协议编程
#客户端
import socket
# 创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET指定使用IPv4协议,SOCK_STREAM指定使用面向流的TCP协议
# 建立连接
s.connect(('127.0.0.1',3806)) # 127.0.0.1是一个特殊的IP地址，表示本机地址
for data in [b'Spike',b'Fye',b'Jet',b'exit']:
    # 发送数据
    s.send(data)
    # 接收数据
    if not data == b'exit':
        print('recv data:',s.recv(1024).decode('utf-8'))
# 关闭连接
s.close()