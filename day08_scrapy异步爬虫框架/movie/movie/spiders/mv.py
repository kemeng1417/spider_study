import scrapy
from movie.items import MovieItem

class MvSpider(scrapy.Spider):
    name = 'mv'

    start_urls = ['http://www.4567kan.com/frim/index8.html']

    url = 'http://www.4567kan.com/frim/index8-%d.html'
    page_num = 2
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'http://www.4567kan.com'+li.xpath('./div/a/@href').extract_first()

            item = MovieItem()
            item['title'] = title

            yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'item':item})
        if self.page_num <=5:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)


    def detail_parse(self, response):
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc

        yield item