import scrapy


# 捕获前五页的数据
class SunSpider(scrapy.Spider):
    name = 'sun'
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1']

    def parse(self, response):
        ul_list = response.xpath('/html/body/div[2]/div[3]/ul[2]')
