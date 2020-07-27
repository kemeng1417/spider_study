import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlPro.items import CrawlproItem,ContentItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1']
    # 实例化一个链接提取器对象

    # 提取页码链接
    link = LinkExtractor(allow=r'id=1&page=\d+')
    detail_link = LinkExtractor(allow=r'index\?id=\d+')
    rules = (
        # 实例化一个Rule对象，调用的是该对象的构造方法
        Rule(link, callback='parse_item', follow=False),
        # follow= True:将每一个页码作为起始的url，可以捕获所有的页码链接
        Rule(detail_link, callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            #使用连接提取器提取url
            item = CrawlproItem()
            item['title'] = title
            yield item
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
    def parse_detail(self, response):
        print(response)
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()

        item = ContentItem()
        item['content'] = content
        yield item


# 注意：不使用请求传参持久化存储可以实现，但是无法实现数据一一对应。
# crawlspider通常和手动传参搭配使用。