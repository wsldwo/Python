#UDP协议编程
#客户端
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # AF_INET指定使用IPv4协议,SOCK_DGRAM指定使用UDP协议
for data in [b'T-800',b'T-1000',b'Rev-9',b'exit']:
    s.sendto(data,('127.0.0.1',3807)) # 直接通过sendto()给服务器发数据
    if not data == b'exit':
        print('recv data:',s.recv(1024).decode('utf-8')) # 从服务器接收数据仍然调用recv()方法
s.close()
print('Client closed!')