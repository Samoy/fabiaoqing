# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    name = scrapy.Field()
    alias = scrapy.Field()


class ListItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()


class EmoticonItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
