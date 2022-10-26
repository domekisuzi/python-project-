import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['4399.com']
    start_urls = ['https://baidu.com/']

    def parse(self, response):
        print("进入了parse阶段")
        print(response.contextcd )
        # s = response.xpath('//div[@class="middle_3 cf"]//li/a/text()').extract()
        # for i in s:
        #     print(i)
