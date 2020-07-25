import time
from multiprocessing.dummy import Pool

import requests


# 普通的同步请求
# urls = [
#     'http://127.0.0.1:5000/jay',
#     'http://127.0.0.1:5000/jj',
#     'http://127.0.0.1:5000/hh',
# ]
#
#
# def get_request(url):
#     page_text = requests.get(url=url).text
#     print(len(page_text))
#
#
# if __name__ == '__main__':
#     start = time.time()
#     for url in urls:
#         get_request(url)
#     end = time.time()
#     print(end - start)


# 基于线程池的异步请求
urls = [
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/jj',
    'http://127.0.0.1:5000/hh',
]


def get_request(url):
    page_text = requests.get(url=url).text
    return len(page_text)


if __name__ == '__main__':
    start = time.time()
    pool = Pool(3) # 启动三个线程
    # 参数1：回调函数
    # 参数2：可迭代对象alist
    # 作用：可以将alist中的每一个元素依次传递给回调函数作为参数，回调函数会异步对列表的元素进行相关操作运算
    # map返回值就是回调函数返回的所有结果
    print(pool.map(get_request, urls))

    print(time.time()-start)
