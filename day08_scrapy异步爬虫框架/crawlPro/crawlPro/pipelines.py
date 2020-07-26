# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlproPipeline:
    def process_item(self, item, spider):
        # 管道可以接收两个不同类型的item，写代码时需要确认接收的item是哪个类型的
        # 必须判断接收的item的类型
        if item.__class__.__name__ == 'ContentItem':
            content = item['content']
            print(content)
        else:
            title = item['title']
            print(title)
        return item
