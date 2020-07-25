# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter



class MiddlewareproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    # 拦截所有请求
    # request就是拦截到的请求
    # 参数spider表示爬虫文件中爬虫类实例化好的爬虫对象，作用：可以实现中间件和爬虫类之间的数据交互
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # request.headers 返回的一个字典，表示的就是拦截的该请求的请求头信息
        # request.headers['User-Agent'] = 'xxx'
        # request.headers['Cookie'] = 'xxx'
        print('i am process_request')
        # print(request.headers)


        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 拦截响应对象
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        print('process_response')
        # response.text = '123'
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response


    # 拦截异常的请求对象,代理请求存放的位置
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        print('I am process_exception!')
        # 需要对异常请求进行修正，需要将修正后的请求重新发送
        # 代理操作写在该方法中
        # request.meta['proxy'] = 'http"//ip:port' # 使用代理实现修正操作
        return request # 对修正后的请求进行重新发送


