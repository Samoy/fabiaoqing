# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    objectId = scrapy.Field()
    order = scrapy.Field()


class GroupItem(scrapy.Item):
    name = scrapy.Field()
    objectId = scrapy.Field()
    parentId = scrapy.Field()
    order = scrapy.Field()


class EmoticonItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    objectId = scrapy.Field()
    parentId = scrapy.Field()
    order = scrapy.Field()
