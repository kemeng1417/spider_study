import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from zlsPro.items import ZlsproItem
class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/frim/index5.html']


    # 创建redis链接
    conn = Redis(host='127.0.0.1', port=6379,password='123456')
    rules = (
        Rule(LinkExtractor(allow=r'frim/index5\-\d+.html'), callback='parse_item', follow=False),
    )

    # 解析电影的名称+detail_url
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url ='http://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()

            # ex=1添加成功，添加的数据不存在
            # ex=0添加失败，添加的数据已经存在
            ex = self.conn.sadd('movie_url',detail_url)
            item = ZlsproItem()
            item['title'] = title
            if ex == 1:
                print('正在爬取')
                yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
            else:
                print('该数据已爬过')

    def parse_detail(self,response):
        item = response.meta['item']

        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc
        yield item