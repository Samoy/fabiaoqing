# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    object_id = scrapy.Field()
    # 次序
    seq = scrapy.Field()


class PackageItem(scrapy.Item):
    name = scrapy.Field()
    object_id = scrapy.Field()
    parent_id = scrapy.Field()
    seq = scrapy.Field()


class EmoticonItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    object_id = scrapy.Field()
    parent_id = scrapy.Field()
    seq = scrapy.Field()


class TagItem(scrapy.Item):
    name = scrapy.Field()
    object_id = scrapy.Field()
