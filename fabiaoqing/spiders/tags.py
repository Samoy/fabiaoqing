# -*- coding: utf-8 -*-
import scrapy
from ..items import TagItem, EmoticonItem
from ..util import md5_encoding


class TagsSpider(scrapy.Spider):
    name = 'tags'
    allowed_domains = ['www.fabiaoqing.com']
    start_urls = ['http://www.fabiaoqing.com/tag']

    def parse(self, response):
        tag_list = response.xpath('//*[@id="bqb"]/div[1]/a')
        for tag in [tag_list[0]]:
            tag_item = TagItem()
            href = tag.xpath('@href').extract_first()
            tag_id = href.strip().split("/")[-1].split(".")[0]
            tag_item['object_id'] = md5_encoding(tag_id)
            tag_item['name'] = tag.xpath('div/text()').extract_first()
            yield tag_item
            yield scrapy.Request(response.urljoin(href), callback=self.parse_emoticon)
        pages = response.xpath('//*[@id="bqb"]/div[3]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href), callback=self.parse)

    def parse_emoticon(self, response):
        images = response.xpath('//*[@id="bqb"]/div[2]/div')
        for image in images:
            href = image.xpath('a/@href').extract_first()
            emoticon_item = EmoticonItem()
            emoticon_item['name'] = image.xpath('a/@title').extract_first()
            obj_id = href.split("/")[-1].split(".")[0]
            emoticon_item['object_id'] = md5_encoding(obj_id)
            emoticon_item['url'] = image.xpath('a/img/@data-original').extract_first()
            emoticon_item['parent_id'] = md5_encoding('tag')
            emoticon_item['seq'] = obj_id
            yield emoticon_item
        pages = response.xpath('//*[@id="bqb"]/div[4]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href), callback=self.parse_emoticon)
