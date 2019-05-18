import scrapy
from ..items import CategoryItem, ListItem, EmoticonItem


class HomeSpider(scrapy.Spider):
    name = "bqb"
    allowed_domains = ["fabiaoqing.com"]
    main_url = "https://fabiaoqing.com/"
    list_url = main_url + 'bqb/lists/'
    start_urls = [list_url]

    def parse(self, response):
        category_list = response.xpath('//*[@id="bqbcategory"]/a')
        # 解析标题数据
        for category in category_list:
            category_item = CategoryItem()
            category_item["name"] = category.xpath('text()').extract_first().strip().replace('\n', '')
            href = category.xpath('@href').extract_first()
            category_item["alias"] = href.strip().split("/")[-1].split(".")[0]
            yield category_item
            yield scrapy.Request(response.urljoin(href), callback=self.parse_list)

    def parse_list(self, response):
        # 解析列表数据
        href = response.css("#bqbcategory > a.item.active").xpath("@href").extract_first()
        alias = href.strip().split("/")[-1].split(".")[0]
        emoticon_list = response.xpath('//*[@id="bqblist"]/a/@href').extract()
        for emoticon in emoticon_list:
            # 请求详情数据
            yield scrapy.Request(response.urljoin(emoticon),
                                 callback=lambda re, category=alias: self.parse_emoticon(re, category))
        # 请求下一页数据
        pages = response.xpath('//*[@id="bqblist"]/div[3]/a')
        for page in pages:
            if "下一页" == page.xpath('text()').extract_first().strip().replace("\n", ""):
                next_href = page.xpath('@href').extract_first().strip()
                yield scrapy.Request(response.urljoin(next_href), callback=self.parse_list)

    # 解析详情数据
    def parse_emoticon(self, response, category):
        img_list = response.xpath('//div[@class="bqppdiv1"]/img')
        list_item = ListItem()
        list_item["category"] = category
        list_item["name"] = response.xpath('//*[@id="bqb"]/div[1]/h1/text()').extract_first()
        yield list_item
        for img in img_list:
            emoticon_item = EmoticonItem()
            emoticon_item["url"] = img.xpath("@data-original").extract_first()
            emoticon_item["name"] = img.xpath("@alt").extract_first()
            emoticon_item["title"] = list_item["name"]
            yield emoticon_item
