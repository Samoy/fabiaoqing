# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import IntegrityError

from .items import CategoryItem, ListItem, EmoticonItem


class FabiaoqingPipeline(object):

    def __init__(self, db_param):
        self.connect = pymysql.connect(
            host=db_param['host'],
            port=db_param['port'],
            db=db_param['db'],
            user=db_param['user'],
            passwd=db_param['passwd'],
            charset=db_param['charset'],
            use_unicode=db_param['use_unicode']
        )
        # 创建一个句柄
        self.cursor = self.connect.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        db_param = dict(
            host=crawler.settings.get('MYSQL_HOST'),
            db=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            passwd=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
            charset='utf8',
            use_unicode=False,
        )
        return cls(db_param)

    def process_item(self, item, spider):
        if isinstance(item, CategoryItem):
            try:
                sql = "insert into category (name,alias) values (%s,%s)"
                self.cursor.execute(sql, (item['name'], item['alias']))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print("该数据已存在")
        elif isinstance(item, ListItem):
            try:
                sql = "insert into list (name,category) values (%s,%s)"
                self.cursor.execute(sql, (item['name'], item["category"]))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print("该数据已存在")
        elif isinstance(item, EmoticonItem):
            try:
                sql = "insert into emoticon(name,url,title) values(%s,%s,%s)"
                self.cursor.execute(sql, (item["name"], item["url"], item["title"]))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print("该数据已存在")
        return item

    def close_spider(self, spider):
        self.connect.close()
