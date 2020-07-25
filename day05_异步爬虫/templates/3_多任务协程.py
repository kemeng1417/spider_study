import requests
import asyncio
import time
import aiohttp
from lxml import etree
# 特殊的函数
# async def get_request(url):
#     print('开始执行')
#     # requests不支持异步的模块
#     page_text = requests.get(url=url).text
#     return page_text

# 特殊的函数：不可以出现不支持异步模块的代码，不可以使用requests模块
async def get_request(url):
    async with aiohttp.ClientSession() as sess: # 实例化一个请求对象sess
        # sess.get(url,headers,params,proxy)
        # sess.post(url,headers,data,proxy)
        # proxy参数的用法和requests用法不一样 proxy='http://ip:port'， proxies={}
        async with await sess.get(url=url) as response: # 调用get发请求，返回一个响应对象
            page_text = await response.text() # text()返回字符串形式的响应数据
            # read()返回bytes类型的响应数据区别于content和json()
            return page_text
# 定义一个任务对象的回调函数
# 注意：回调函数必须要求一个函数，参数表示的是该函数的绑定者
# 多任务的异步爬虫中数据解析或者持久化存储的操作需要写在回调函数中
def parse(task):
    # result():返回的就是特殊函数的返回值
    page_text = task.result()
    tree = etree.HTML(page_text)
    data_text = tree.xpath('//div[@id="rs"]//text()')
    print(data_text)
if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/jj',
        'http://127.0.0.1:5000/hh',
    ]
    # 定义一个任务列表
    tasks = []
    for url in urls:

        # 返回三个协程对象
        c = get_request(url)


        # 创建三个任务对象（基于已有的对象创建任务对象）必须先有协程对象，再创建任务对象
        task = asyncio.ensure_future(c)

        # 给该任务对象绑定一个回调函数
        task.add_done_callback(parse)
        tasks.append(task)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务列表中的多个任务注册到eventloop且启动该对象
    # loop.run_until_complete(tasks)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start)