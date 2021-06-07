# PIL Python Imaging Library
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#绘制验证码图片

#随机大写字母
def rndChar():
    return chr(random.randint(65,90))# ansi编码 A~Z [65,90] a~z [97,122]
#随机颜色
def rndColor():
    return (random.randint(50,200),random.randint(50,200),random.randint(50,200))
def rndColor2():
    return (random.randint(20,100),random.randint(20,100),random.randint(20,100))
width = 60 * 3
height = 60
# 1、创建Image对象
image = Image.new('RGB',(width,height),(255,255,255))
# 2、创建Draw对象
draw = ImageDraw.Draw(image)
# 3、创建Font对象
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf',36)

# 填充图片像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
# 输出文字
for x in range(3):
    draw.text((60*x+10,10),rndChar(),font=font,fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
# 保存
image.save('code.jpg','jpeg') #会不断覆盖已有图片

# requests 简单好用的网络请求模块
# get请求
import requests
r = requests.get('https://www.gamersky.com/')
print(r.status_code)
print(r.encoding)
print(r.content[:100])
print(r.text[:100])
# params传参
r = requests.get('https://www.3dmgame.com/',params={'arg1':'100','arg2':'101'})
print(r.url)
print(r.status_code)
print(r.encoding)
print(r.content[:100])
print(r.text[:100])
# get添加HTTP Header(模拟iphone访问)
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.status_code)
print(r.encoding)
print(r.content[:100])
print(r.text[:100])

# post请求 
r = requests.post('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.status_code)
print(r.encoding)
print(r.content[:100])
print(r.text[:100])
# data传参 
r = requests.post('https://www.gamersky.com/',
data={'form_email': 'abc@example.com', 'form_password': '123456'},
cookies={'token': '12345', 'status': 'working'},
timeout=2.5)
print(r.url)
print(r.status_code)
print(r.encoding)
print(r.headers)
print(r.content[:100])
print(r.text[:100])

