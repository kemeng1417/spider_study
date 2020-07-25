# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


# 存储到本地文件
class DuanziproPipeline:
    fp = None

    # 重写父类一个方法：只会在爬虫开始后被执行一次
    def open_spider(self, spider):
        print('i am open_spider')
        self.fp = open('./duanzi.txt', 'w', encoding='utf-8')

    # 这个方法是用来接收爬虫文件提交过来的item对象（一次只能接收一个item对象）
    # 参数：item就是接收到的item对象
    def process_item(self, item, spider):
        print('i am process_item')
        # 将接收到的item对象写入文件
        title = item['title']  # 将item对象中存储的值取出
        content = item['content']

        self.fp.write(title + ':' + content + '\n')
        # open('./te.txt') # 写在此处不合适，因为process_item方法会被调用多次
        return item

    # 重写父类的一个方法:只会在爬虫结束前调用一次
    def close_spider(self, spider):
        print('i am close_spider')
        self.fp.close()


# 存储到mysql数据库中
class MysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='spider',
                                    charset='utf8')
        print(self.conn)

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        sql = 'insert into duanzi values("{}","{}");'.format(title, content)

        # 执行mysql语句
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
