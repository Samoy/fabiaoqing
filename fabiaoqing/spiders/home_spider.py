# -*- coding: utf-8 -*-
import scrapy

from ..util import md5_encoding
from ..items import CategoryItem, PackageItem, EmoticonItem


class HomeSpider(scrapy.Spider):
    name = "bqb"
    allowed_domains = ["fabiaoqing.com"]
    main_url = "https://fabiaoqing.com/"
    list_url = main_url + 'bqb/lists/'
    start_urls = [list_url]

    def parse(self, response):
        category_list = response.xpath('//*[@id="bqbcategory"]/a')
        # 解析标题数据
        for (index, category) in enumerate(category_list):
            category_item = CategoryItem()
            category_item["name"] = category.xpath('text()').extract_first().strip().replace('\n', '')
            href = category.xpath('@href').extract_first()
            category_item["object_id"] = md5_encoding(href.strip().split("/")[-1].split(".")[0])
            category_item["seq"] = index + 1
            yield category_item
            yield scrapy.Request(response.urljoin(href),
                                 callback=lambda re, ca=category_item: self.parse_package(re, ca))

    def parse_package(self, response, category):
        emoticon_group = response.xpath('//*[@id="bqblist"]/a/@href').extract()
        for index, group in enumerate(emoticon_group):
            package_item = PackageItem()
            group_id = group.split("/")[-1].split(".")[0]
            package_item["object_id"] = md5_encoding(group_id)
            package_item["parent_id"] = category["object_id"]
            package_item["name"] = response.xpath(
                '//*[@id="bqblist"]/a[%d]/div/header/h1/text()' % (index + 1)).extract_first().strip().replace('\n', '')
            package_item["seq"] = group_id
            yield package_item
            # 请求详情数据
            yield scrapy.Request(response.urljoin(group),
                                 callback=lambda re, p_id=package_item["object_id"]: self.parse_emoticon(re, p_id))
        # 请求下一页数据
        pages = response.xpath('//*[@id="bqblist"]/div[3]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href),
                                     callback=lambda re, ca=category: self.parse_package(re, ca))

    # 解析详情数据
    def parse_emoticon(self, response, package_id):
        img_group = response.xpath('//div[@class="bqppdiv1"]/img')
        for index, img in enumerate(img_group):
            emoticon_item = EmoticonItem()
            emoticon_item["url"] = img.xpath("@data-original").extract_first()
            emoticon_item["name"] = img.xpath("@alt").extract_first()
            href = img_group.xpath('../../a[%d]/@href' % (index + 1)).extract_first()
            obj_id = href.split("/")[-1].split(".")[0]
            emoticon_item["object_id"] = md5_encoding(obj_id)
            emoticon_item["parent_id"] = package_id
            emoticon_item["seq"] = obj_id
            yield emoticon_item
