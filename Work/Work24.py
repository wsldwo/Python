#爬虫入门 (糗事百科)
import requests
import time
import re
from bs4 import BeautifulSoup

def retrieve(url):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    respond = requests.get(url,headers = headers)
    content = respond.text

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all(attrs={'class':'article block untagged mb15 typs_hot'})

    jokes = ''

    for div in divs:
        if div.find_all(attrs={'class':'contentForAll'}):#不完整笑话
            joke = '\nnot finished joke:\n'+div.span.get_text()
            print(joke)
            #print('---------------------')
            #@@@@@@@@##########$$$$$$$$$$$
            #获取完整的笑话内容
            contentHerf = div.find(attrs={'class':'contentHerf'})
            #print('not finished joke href:')
            herf = str(contentHerf)[23:48]#链接切片
            #print(herf)
            herfpath = herf[6:-1]#链接切片
            joke += '\nfinished joke:\n'+ retrieveComplete('https://www.qiushibaike.com'+herfpath)#获取完整笑话
        else:
            joke = div.span.get_text()
        jokes += joke
    writeFiletxt(jokes)


def retrieveComplete(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    respond = requests.get(url,headers = headers)
    content = respond.text

    #print('\n$$$$$$$$##########@@@@@@@@@@@!!!!!!!!!/n\n')
    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all(attrs={'class':'content'})

    #fulljokes = ''
    print('full joke:')
    divsstr = str(divs)[22:-7].replace('<br/>','')#剔除标签
    print(divsstr)
    print('\n\n')
    return divsstr

def deleteTag(str):
    pass
    

def writeFiletxt(s):
    with open('jokefile.txt','a',encoding='utf-8') as f:# appending 追加模式
        f.write('\n') #换行
        f.write(s)

start = 30
end = start + 10
while(start <= end):
    if(start > 0):
        url = 'https://www.qiushibaike.com/text/'+'page/'+str(start)+'/'
    else:
        url = 'https://www.qiushibaike.com/text/'
    writeFiletxt('---------------------count='+str(start)+'-------Begin------------')
    retrieve(url)
    time.sleep(3)
    writeFiletxt('---------------------count='+str(start)+'--------End-----------')
    start += 1