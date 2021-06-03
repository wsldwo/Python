#爬虫入门 (煎蛋网)
import requests
import time
import re
from bs4 import BeautifulSoup

def retrieve(url,page):

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    respond = requests.get(url,headers = headers)
    content = respond.text

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find_all(attrs={'class':'post f list-post'})

    
    for div in divs:
        divstr = str(div)[0:150].split(' ')#切片再用空格分割
        if(page == 1):
            href = str(divstr[5])
            retrieveArticle(href[6:-1])
        else:
            href = str(divstr[8])
            retrieveArticle(href[6:-1])

    

def pickupLink(str):
    pass

def retrieveArticle(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'}#字典类型
    respond = requests.get(url,headers = headers)
    content = respond.text

    soup = BeautifulSoup(content,'lxml')#lxml为解析器
    divs = soup.find(attrs={'class':'post f'})

    article = ''

    #打印标题
    if divs.find('h1'):
        title = str(divs.find('h1')).split('>')
        titlestr = title[2]#选择list第3个元素
        titlestr = titlestr[0:-3]#进行切片，得到标题

        article += '标题：'+titlestr+'\n正文：\n'
    #打印正文
    for p in divs.find_all('p'):
        paragraphs = str(p)
        
        for a in p.find_all('a'):#删除p标签中的a标签
            print(str(a))
            paragraphs = paragraphs.replace(str(a).split('>')[0]+'>','')

        for i in p.find_all('img'):#删除p标签中的img标签
            print(str(i))
            paragraphs = paragraphs.replace(str(i),'')
            
        paragraphs = paragraphs.replace('<p>','')
        paragraphs = paragraphs.replace('</p>','')
        paragraphs = paragraphs.replace('</strong>','')
        paragraphs = paragraphs.replace('<strong>','')
        paragraphs = paragraphs.replace('<br/>','')
        paragraphs = paragraphs.replace('<em>','')
        paragraphs = paragraphs.replace('</em>','')
        paragraphs = paragraphs.replace('</a>','')

        article += paragraphs+'\n'

    writeFiletxt(article)
    
def writeFiletxt(s):
    with open('jandanfile.txt','a',encoding='utf-8') as f:# appending 追加模式
        f.write('\n') #换行
        f.write(s)

page = 7
end = page + 3
while(page <= end):
    if(page > 1):
        url = 'http://jandan.net/page/'+str(page)
    else:
        url = 'http://jandan.net/'
    writeFiletxt('---------------------page='+str(page)+'-------Begin------------')
    retrieve(url,page)
    time.sleep(3)
    writeFiletxt('---------------------page='+str(page)+'--------End-----------')
    page += 1