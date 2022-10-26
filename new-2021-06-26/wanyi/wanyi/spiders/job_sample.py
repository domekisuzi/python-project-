import scrapy
from wanyi.items import  WanyiSimpleItem

class JobSampleSpider(scrapy.Spider):
    name = 'job_sample'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        my_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        for num, node in enumerate(my_list):
            if num % 2 == 0:
                item = WanyiSimpleItem()
                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                # response.urljoin用于凭借相对路径的url,可以理解未自动补全
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
                item['depart'] = node.xpath('./td[2]/text()').extract_first()
                item['category'] = node.xpath('./td[3]/text()').extract_first()
                item['type'] = node.xpath('./td[4]/text()').extract_first()
                item['address'] = node.xpath('./td[5]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()
                item['date'] = node.xpath('./td[7]/text()').extract_first()
                # print('-------------')
                # print('我在parse中' )
                # print('-------------')
                print(item)
                yield  item
                # 构建详情页面的请求

        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()
        # 判断终止条件
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            # 构建请求对象,并且返回给引擎
            # print('-------------')
            # print('我在parse中的翻页')
            # print('-------------')
            yield scrapy.Request(url=next_url, callback=self.parse)


