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
            category_item["order"] = index + 1
            yield category_item
            yield scrapy.Request(response.urljoin(href), callback=lambda re, ca=category_item: self.parse_group(re, ca))

    # todo:添加分组排序
    def parse_group(self, response, category):
        # 当前页，为了排序使用，排序方法为当前页码乘以下标
        current_page = response.css('#bqblist > div.ui.pagination.menu > a.active.item').xpath(
            'text()').extract_first().strip().replace('\n', '')
        emoticon_group = response.xpath('//*[@id="bqblist"]/a/@href').extract()
        for index, group in enumerate(emoticon_group):
            group_item = GroupItem()
            group_id = group.split("/")[-1].split(".")[0]
            group_item["objectId"] = md5_encoding(group_id)
            group_item["parentId"] = category["objectId"]
            group_item["name"] = response.xpath(
                '//*[@id="bqblist"]/a[%d]/div/header/h1/text()' % (index + 1)).extract_first().strip().replace('\n', '')
            # 此处不用index直接乘上页码是由于0乘以任何数都为0
            order = (index + 1) * int(current_page)
            group_item["order"] = order
            yield group_item
            # 请求详情数据
            yield scrapy.Request(response.urljoin(group),
                                 callback=lambda re, g_id=group_item["objectId"], i=index: self.parse_emoticon(re, g_id,
                                                                                                               i))
        # 请求下一页数据
        pages = response.xpath('//*[@id="bqblist"]/div[3]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href),
                                     callback=lambda re, ca=category: self.parse_group(re, ca))

    # 解析详情数据
    # todo:添加表情包排序
    def parse_emoticon(self, response, group_id, group_index):
        img_group = response.xpath('//div[@class="bqppdiv1"]/img')
        for index, img in enumerate(img_group):
            emoticon_item = EmoticonItem()
            emoticon_item["url"] = img.xpath("@data-original").extract_first()
            emoticon_item["name"] = img.xpath("@alt").extract_first()
            href = img_group.xpath('../../a[%d]/@href' % (index + 1)).extract_first()
            emoticon_item["objectId"] = md5_encoding(href.split("/")[-1].split(".")[0])
            emoticon_item["parentId"] = group_id
            emoticon_item["order"] = group_index * (index + 1)
            yield emoticon_item
