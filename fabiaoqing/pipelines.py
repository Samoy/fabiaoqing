# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import IntegrityError

from .items import CategoryItem, PackageItem, EmoticonItem, TagItem


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
                sql = "insert into t_category (object_id,name,seq) values (%s,%s,%s)"
                self.cursor.execute(sql, (item['object_id'], item['name'], item['seq']))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print("该数据已存在")
        elif isinstance(item, PackageItem):
            try:
                sql = "insert into t_package (object_id,name,parent_id,seq) values (%s,%s,%s,%s)"
                self.cursor.execute(sql, (item["object_id"], item['name'], item["parent_id"], item["seq"]))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print('该数据已存在')
        elif isinstance(item, TagItem):
            try:
                sql = "insert into t_tag (object_id,name) values (%s,%s)"
                self.cursor.execute(sql, (item['object_id'], item['name']))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print("该数据已存在")
        elif isinstance(item, EmoticonItem):
            try:
                sql = "insert into t_emoticon(object_id,name,url,parent_id,seq) values(%s,%s,%s,%s,%s)"
                self.cursor.execute(sql, (item["object_id"], item["name"], item["url"], item["parent_id"], item["seq"]))
                self.connect.commit()
            except IntegrityError as error:
                if error.args[0] == 1062:
                    print('该数据已存在')
        return item

    def close_spider(self, spider):
        self.connect.close()
