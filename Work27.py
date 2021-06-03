#爬虫入门（koikastu）
import requests
import time
import re
import os
import rarfile
import shutil
from bs4 import BeautifulSoup

def writeFilePics(filename,url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))#设置超时 连接超时=5s、读取超时=5s
    except requests.exceptions.RequestException as e:
        print('writeFilePics:'+str(e)+'timeout!!!!!!')
        return#直接返回
    with open('koikastu/'+filename,'wb') as f:# wb 写二进制
        f.write(respond.content)


def retrieve(url):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))#设置5秒超时（连接超时=5s、读取超时=5s）
    except requests.exceptions.RequestException as e:
        print('retrieve:'+str(e)+'timeout!!!!!!')
        return#直接返回
    content = respond.content.decode('utf-8') #解决Requests中文乱码 分析requests的源代码发现，text返回的是处理过的Unicode型的数据，而使用content返回的是bytes型的原始数据。

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all('span',class_='thumb')#attrs={'class':'box picblock col3 masonry-brick'}

    for div in divs:
        a = div.find('a')
        if a:
            href = (website + str(a).split(' ')[1][6:-1]).replace('amp;','') #分割+切片 提取链接
            print(href)
            retrievePic(href)

       
def retrievePic(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))
    except requests.exceptions.RequestException as e:
        print('retrievePic:'+str(e)+'timeout!!!!!!')
        return#直接返回
    content = respond.content.decode('utf-8')
    
    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    a = soup.find('img',id='image')
    picurl = str(a).split(' ')[4][5:-1]
    print(picurl+'######'+picurl.split('/')[-1])
    writeFilePics(picurl.split('/')[-1],picurl)

if not os.path.exists('koikastu'):
    os.mkdir('koikastu')

page = 1
end = page + 13
website = 'https://illusioncards.booru.org/'

download_path = 'E:\Py Projects\koikastu'
while(page <= end):
    if(page > 1):
        url = 'https://illusioncards.booru.org/index.php?page=post&s=list&tags=koikatsu+scene&pid='+str(page*10)
    else:
        url = 'https://illusioncards.booru.org/index.php?page=post&s=list&tags=koikatsu+scene&pid=0'
    print('-------------Page'+str(page)+'------BEGIN-----------')
    retrieve(url)
    print('-------------Page'+str(page)+'------END------------')
    #time.sleep(3)#限制访问频率
    page += 1


