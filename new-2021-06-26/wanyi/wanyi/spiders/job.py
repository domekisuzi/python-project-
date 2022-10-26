import scrapy
from wanyi.items import WanyiItem


# 如果未返回过item,则不会进入pipeline
class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']
    #用于翻页,解析数据
    def parse(self, response):
        my_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        print('my_list的url为: ' + response.url)
        for num, node in enumerate(my_list):
            if num % 2 == 0:
                item = WanyiItem()
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
                # print('我在parse中')
                # print('-------------')
                # print(item)
                # yield  item
                # 构建详情页面的请求,解析详情页后返回同一个界面
                yield scrapy.Request(url=item['link'], callback=self.parse_detail, meta={'item': item})
                print('----------------------')
                # 模拟翻页,注意这个last
        print('************************')
        part_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()
        # 判断终止条件
        print('part_url的url为: ' + response.url)
        if part_url != 'javascript:void(0)':
            next_url = response.urljoin(part_url)
            # 构建请求对象,并且返回给引擎
            # print('-------------')
            # print('我在parse中的翻页')
            # print('-------------')
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        # print('-------------')
        # print('我在自定义parse中')
        # print('-------------')
        # 将meta传参获取
        # print(response.text)
        print('=============')
        item = response.meta['item']
        print("原网址为" + item['link'])
        # extract后记得加()
        # 提取剩余字段
        item['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        # print(item)
        # 返回给引擎
        print('detail的url为: ' + response.url)
        yield item
