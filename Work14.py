# chardet 检测编码
import chardet
data = b'Hello,World!'
print(chardet.detect(data))
data = '窗前明月光，疑是地上霜'.encode('gbk')
print(chardet.detect(data))
data = '鹅鹅鹅，曲项向天歌'.encode('utf-8')
print(chardet.detect(data))
data = 'また夜が明ければお別れ 夢は遠きまぼろしに'.encode('euc-jp')
print(chardet.detect(data))

# psutil 获取系统信息 process and system utilities
import psutil
# 获取CPU信息
print('CPU物理核心数：%s，CPU逻辑核心数：%s' % (psutil.cpu_count(logical=False),psutil.cpu_count()))
# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())
# 统计CPU使用率 累计10次，间隔1秒
for x in range(3):
    print(psutil.cpu_percent(interval=1,percpu=True))

# 获取物理内存
print(psutil.virtual_memory()) #单位字节
# 获取交换内存
print(psutil.swap_memory()) #单位字节

# 磁盘分区信息
print(psutil.disk_partitions()) #单位字节
# 磁盘使用情况
print(psutil.disk_usage('E:')) #单位字节
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络读写字节／包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 获取当前网络连接信息
print(psutil.net_connections())

print('-----------@@@@@@-----------')
# 获取所有进程ID
print(psutil.pids())
# 获取指定进程ID=135220
print(psutil.Process(135220))
# 打印进程
psutil.test()


# virtualenv
# 可以针对每个应用创建独立的Python运行环境
# 为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题

# 1、创建独立Python环境，命名为env1
# virtualenv env1

#-p 指定所用的python解析器的版本,默认使用的是当前系统安装(/usr/bin/python)的python解析器 
#virtualenv -p C:\Users\WJ\AppData\Local\Programs\Python\Python36\python.exe venv

# 2、启动环境
# env1\Scripts\activate
# 3、进行开发

# 4、退出环境
#deactivate
