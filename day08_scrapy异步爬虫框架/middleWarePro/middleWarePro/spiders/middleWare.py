import scrapy


class MiddlewareSpider(scrapy.Spider):
    name = 'middleWare'
    url = 'xxx'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https123://www.baidu.com/']

    def parse(self, response):
        pass
