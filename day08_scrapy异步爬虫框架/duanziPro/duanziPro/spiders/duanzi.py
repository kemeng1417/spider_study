import scrapy
from duanziPro.items import DuanziproItem

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://ishuo.cn/xiaozhishi']

    # 数据解析操作
    # def parse(self, response):
    #     # 实现诗句解析：段子的内容和标题
    #     # 不同于etree.xpath()，但是使用上基本一致，只有细微的差异
    #     li_list = response.xpath('//*[@id="list"]/ul/li')
    #     for li in li_list:
    #         # 返回的是一个Selector对象，且提取的字符串参数被存储在该对象中
    #         # content = li.xpath('./div[1]/text()')[0]
    #         # 返回字符串数据
    #         # content = li.xpath('./div[1]/text()')[0].extract()
    #         # extract_first()将列表中的第0个元素进行数据提取
    #         content = li.xpath('./div[1]/text()').extract_first()
    #         # extract()将列表中每一个列表元素表示的Selector对象的字符串取出
    #         title = li.xpath('./div[2]/span//text()').extract() # 返回的是列表，列表中有多个元素
    #         title = ''.join(title) # 将列表转换为字符串
    #         print('内容',content)
    #         print('标题',title)

    # # 基于终端指令
    # def parse(self, response):
    #     all_data = []
    #     # 实现诗句解析：段子的内容和标题
    #     # 不同于etree.xpath()，但是使用上基本一致，只有细微的差异
    #     li_list = response.xpath('//*[@id="list"]/ul/li')
    #     for li in li_list:
    #         # 返回的是一个Selector对象，且提取的字符串参数被存储在该对象中
    #         # content = li.xpath('./div[1]/text()')[0]
    #         # 返回字符串数据
    #         # content = li.xpath('./div[1]/text()')[0].extract()
    #         # extract_first()将列表中的第0个元素进行数据提取
    #         content = li.xpath('./div[1]/text()').extract_first()
    #         # extract()将列表中每一个列表元素表示的Selector对象的字符串取出
    #         title = li.xpath('./div[2]/span//text()').extract() # 返回的是列表，列表中有多个元素
    #         title = ''.join(title) # 将列表转换为字符串
    #         dic = {
    #             'content': content,
    #             'title': title,
    #         }
    #         all_data.append(dic)
    #     return all_data # 返回值就是解析到的所有的数据

    # 基于管道的持久化存储
    def parse(self, response):
        li_list = response.xpath('//*[@id="list"]/ul/li')
        for li in li_list:
            content = li.xpath('./div[1]/text()').extract_first()

            title = li.xpath('./div[2]/span//text()').extract()  # 返回的是列表，列表中有多个元素
            title = ''.join(title)  # 将列表转换为字符串

            # 将解析到的数据存储到Item对象
            item = DuanziproItem()
            # 注意：访问item对象中的title属性，只能使用中括号的方式
            item['title'] = title
            item['content'] = content

            # 将Item对象提交给管道,pipelines.py定义好了管道类
            yield item
