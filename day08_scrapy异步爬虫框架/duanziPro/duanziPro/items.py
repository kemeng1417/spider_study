# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DuanziproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义好了两个属性，用来存储解析到的两个数据
    title = scrapy.Field()
    content = scrapy.Field()
