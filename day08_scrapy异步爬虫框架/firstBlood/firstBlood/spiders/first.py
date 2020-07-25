import scrapy


class FirstSpider(scrapy.Spider):
    # 表示爬虫文件的名称，爬虫文件的唯一标识
    name = 'first'
    # 允许的域名：用来做请求限定，一旦该域名定义好之后，则start_url只可以发起该域名下的get请求
    # allowed_domains = ['www.xxx.com']
    # 起始url列表：将想要爬取的url，存放在该列表中，这个列表可以帮我们进行get请求发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']

    # 用作于数据解析，response参数就是请求回来的响应对象
    def parse(self, response):
        print(response)
