import scrapy


class HomeSpider(scrapy.Spider):
    name = "biaoqing"
    allowed_domains = ["fabiaoqing.com"]
    start_urls = ['https://fabiaoqing.com/bqb/lists']

    def parse(self, response):
        title_list = response.xpath('//*[@id="bqbcategory"]/a')
        for title in title_list:
            print(title.xpath('text()').extract()[0].strip().replace('\n', ''))
