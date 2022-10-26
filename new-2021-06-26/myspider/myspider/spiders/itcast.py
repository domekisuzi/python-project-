import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml#ajavaee']

    #解析方法

    def parse(self, response):
        #定义对于响应网站的相关操作
        # with open('itcast.html','wb') as f:
        #     f.write(response.body)
        #     print('成功')
        node_list = response.xpath('//div[@class="li_txt"]')
        print(node_list)
        for node in node_list:
            #xpath返回的是选择器对象列表,extract用于向选择器提取数据
            #extract_first 如果无则自动为null
            #yield 相当于return, 可以多次执行的return
            item = MyspiderItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()')[0].extract()
            item['desc'] = node.xpath('./p/text()')[0].extract()
            yield item
