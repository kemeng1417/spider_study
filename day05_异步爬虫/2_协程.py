import requests
import asyncio
import time

# 特殊的函数
async def get_request(url):
    print('开始执行')
    page_text = requests.get(url=url).text
    return page_text
# 定义一个任务对象的回调函数
# 注意：回调函数必须要求一个函数，参数表示的是该函数的绑定者
def parse(task):
    # result():返回的就是特殊函数的返回值
    page_text = task.result()
    print('task的回调函数',page_text)

if __name__ == '__main__':
    # 返回一个协程对象
    c = get_request('http://127.0.0.1:5000/jay')


    # 创建一个任务对象（基于已有的对象创建任务对象）必须先有协程对象，再创建任务对象
    task = asyncio.ensure_future(c)

    # 给该任务对象绑定一个回调函数
    task.add_done_callback(parse)

    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将task存储到eventloop且启动该对象
    loop.run_until_complete(task)