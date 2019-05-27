import scrapy

from ..util import md5_encoding
from ..items import CategoryItem, GroupItem, EmoticonItem


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
            category_item["objectId"] = md5_encoding(href.strip().split("/")[-1].split(".")[0])
            category_item["order"] = index
            yield category_item
            yield scrapy.Request(response.urljoin(href), callback=self.parse_group)

    # todo:添加分组排序
    def parse_group(self, response):
        # 解析列表数据
        href = response.css("#bqbcategory > a.item.active").xpath("@href").extract_first()
        alias = href.strip().split("/")[-1].split(".")[0]
        emoticon_group = response.xpath('//*[@id="bqblist"]/a/@href').extract()
        for emoticon in emoticon_group:
            # 请求详情数据
            yield scrapy.Request(response.urljoin(emoticon),
                                 callback=lambda re, category=alias: self.parse_emoticon(re, category))
        # 请求下一页数据
        pages = response.xpath('//*[@id="bqblist"]/div[3]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href), callback=self.parse_group)

    # 解析详情数据
    # todo:添加表情包排序
    def parse_emoticon(self, response, category):
        img_group = response.xpath('//div[@class="bqppdiv1"]/img')
        group_item = GroupItem()
        group_id = md5_encoding(response.url.strip().split("/")[-1].split(".")[0])
        group_item["objectId"] = group_id
        group_item["parentId"] = md5_encoding(category)
        group_item["name"] = response.xpath('//*[@id="bqb"]/div[1]/h1/text()').extract_first()
        yield group_item
        for index, img in enumerate(img_group):
            emoticon_item = EmoticonItem()
            emoticon_item["url"] = img.xpath("@data-original").extract_first()
            emoticon_item["name"] = img.xpath("@alt").extract_first()
            href = img_group.xpath('../../a[' + str(index + 1) + ']/@href').extract_first()
            emoticon_item["objectId"] = md5_encoding(href.split("/")[-1].split(".")[0])
            emoticon_item["parentId"] = group_item["objectId"]
            yield emoticon_item
