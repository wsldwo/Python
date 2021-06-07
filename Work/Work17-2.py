#UDP协议编程
#服务器
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # AF_INET指定使用IPv4协议,SOCK_DGRAM指定使用UDP协议
# 监听端口
s.bind(('127.0.0.1',3807))
# 不需要调用listen()方法
#s.listen(4)
while True:
    # 不需要接受一个新连接:
    #sock,addr = s.accept()
    # 直接接收来自任何客户端的数据
    data,addr = s.recvfrom(1024)
    print('Received data:%s from %s' % (data,addr))
    if not data.decode('utf-8') == 'exit':
        s.sendto(b'Hello,%s!'% data,addr)
    else:
        break
    #print('#######@@@@@$$$$$$')
    #break # 防止程序无法退出
