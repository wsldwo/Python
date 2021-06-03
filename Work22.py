# aiohttp
# asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。
# 如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

import asyncio
from aiohttp import web

async def home(request):
    return web.Response(body=b'<h1>Home!</h1>',content_type='text/html')
async def hello(request):
    text = '<h1>Hello,%s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')
def init():
    app = web.Application()
    app.add_routes([web.get('/',home),
                    web.get('/hello/{name}',hello)])   
    web.run_app(app,host='127.0.0.1',port=8888)
    
init()
