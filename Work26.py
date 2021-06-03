#爬虫入门（站长素材）
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
    with open('汽车图片/'+filename,'wb') as f:# wb 写二进制
        f.write(respond.content)

def writeFilePicsFHD(filename,url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))#设置超时 连接超时=5s、读取超时=10s
    except requests.exceptions.RequestException as e:
        print('writeFilePicsFHD:'+str(e)+'timeout!!!!!!')
        return#直接返回
    with open('下载/'+filename,'wb') as f:# wb 写二进制
        f.write(respond.content)
    

def retrieve(url,FHD=False):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))#设置5秒超时（连接超时=5s、读取超时=5s）
    except requests.exceptions.RequestException as e:
        print('retrieve:'+str(e)+'timeout!!!!!!')
        return#直接返回
    content = respond.content.decode('utf-8') #解决Requests中文乱码 分析requests的源代码发现，text返回的是处理过的Unicode型的数据，而使用content返回的是bytes型的原始数据。

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all('div',class_='box picblock col3')#attrs={'class':'box picblock col3 masonry-brick'}

    for div in divs:
        a = div.find('a')
        href = str(a).split(' ')[2][6:-1]
        if not FHD:
            retrievePic(href)
        else:
            retrievePicFHD(href)
    
def retrievePic(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))
    except requests.exceptions.RequestException as e:
        print('retrievePic:'+str(e)+'timeout!!!!!!')
        return#直接返回
    content = respond.content.decode('utf-8')

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    a = soup.find('a',class_='image_gall')
    print(str(a).split(' ')[2][6:-1]+' @@@ '+str(a).split(' ')[3][7:-10])
    writeFilePics(str(a).split(' ')[3][7:-10]+'.jpg',str(a).split(' ')[2][6:-1])

def retrievePicFHD(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    try:
        respond = requests.get(url,headers = headers,timeout = (5,5))
    except requests.exceptions.RequestException as e:
        print('retrievePicFHD:'+str(e)+'timeout!!!!!!')
        return#直接返回
    content = respond.content.decode('utf-8')
    #print(content)
    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all('div',class_='dian')
    print(str(list(divs)[1]).split(' ')[2][6:-1])
    #print(str(list(divs)[1]).split(' ')[2][6:-1][52:])
    writeFilePicsFHD(str(list(divs)[1]).split(' ')[2][6:-1][52:],str(list(divs)[1]).split(' ')[2][6:-1])
    #for div in divs:
        #print(div)
    #print(str(a).split(' ')[2][6:-1]+' @@@ '+str(a).split(' ')[3][7:-10])
    #writeFilePics(str(a).split(' ')[3][7:-10]+'.jpg',str(a).split(' ')[2][6:-1])


if not os.path.exists('汽车图片'):
    os.mkdir('汽车图片')
if not os.path.exists('汽车图片FHD'):
    os.mkdir('汽车图片FHD')
if not os.path.exists('下载'):
    os.mkdir('下载')


def unrar(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(download_path,file)):#传入绝对路径
            try:
                rf = rarfile.RarFile(os.path.join(download_path,file))#传入绝对路径
                rf_list = rf.namelist()
                print(rf_list)
                rf.extract(rf_list[0],fhd_path)
                pic_path = str(rf_list[0]).split('/')
                print(pic_path)
                if not os.path.isfile(fhd_path+'/'+pic_path[1]):#检测外面是否有同名文件
                    shutil.move(fhd_path+'/'+pic_path[0]+'/'+pic_path[1],fhd_path)#移动图片到外面
                else:
                    if not os.path.isfile(fhd_path+'/'+pic_path[1][0:-4]+'rename.jpg'):
                        print('file already exists!!!!! renaming---------->')
                        shutil.move(fhd_path+'/'+pic_path[0]+'/'+pic_path[1],fhd_path+'/'+pic_path[1][0:-4]+'rename.jpg')#重命名并移动图片到外面
                    else:
                        print('file already exists!!!!! skipping---------->')

                shutil.rmtree(fhd_path+'/'+pic_path[0])#删除原文件夹
            
            except Exception as e:
                print('error@@@@@@@@@@@@error'+str(pic_path)+'error############error')#非常重要！！！！预防Crash!!!
                print(e)
                continue

page = 15
end = page + 0
fhd = True
work_path = 'E:\Py Projects'
fhd_path = 'E:\Py Projects\汽车图片FHD'
download_path = 'E:\Py Projects\下载'
while(page <= end):
    if(page > 1):
        url = 'http://sc.chinaz.com/tupian/QiCheTuPian_'+str(page)+'.html'
    else:
        url = 'http://sc.chinaz.com/tupian/QiCheTuPian.html'
    print('-------------Page'+str(page)+'------BEGIN-----------')
    retrieve(url,fhd)
    print('-------------Page'+str(page)+'------END------------')
    #time.sleep(3)#限制访问频率
    page += 1

if fhd:
    print('Begin Extract......')
    unrar(download_path)
    #print(os.listdir('汽车图片FHD'))
    print('End Extract......')
    #删除下载目录
    shutil.rmtree(download_path)

