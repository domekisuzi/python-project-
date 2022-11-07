import scrapy
from shixun.log import logger
from shixun.items import SouHuItem


class SouhuSpider(scrapy.Spider):
    name = 'souhu'
    # allowed_domains = ['souhu.com']
    # start_urls = ['http://souhu.com/']
    urls = []

    def __init__(self):  # 初始化,用于获取url列表
        f = open(r'D:\python_project\all\python-project-\new-2021-06-26\shixun\shixun\spiders\url1.text', 'r',encoding='utf-8')
        while True:
            s = f.readline().replace('\n', '')
            if s:
                self.urls.append(s)
            else:
                break

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse,meta={f'lag':False})

    def parse(self, response):
        # 获取详情页
        detail_page = response.xpath(
            '//*[@id="contentA"]/div[1]/div[3]/div[1]/div[2]/div/ul[3]/li/a/@href').extract_first()
        url = "https:" + detail_page
        yield scrapy.Reques+t(url=url, callback=self.detail_parse,meta={'flag':True})

    def detail_parse(self, response):
        name = response.xpath('//*[@id="BIZ_IS_Name"]/text()').extract_first()
        trs = response.xpath('//*[@id="BIZ_hq_historySearch"]/tbody/tr')
        logger.critical("trs为" + str(trs))
        for td in trs[2::]:
            item = SouHuItem()
            item['name'] = name  #名称
            item['date'] = td.xpath('./td[1]/text()').extract_first()  #日期
            item['opening_price'] = td.xpath('./td[2]/text()').extract_first()#开盘价
            item['closing_price'] = td.xpath('./td[3]/text()').extract_first()#收盘价
            item['ups_and_downs'] = td.xpath('./td[4]/text()').extract_first()#涨跌幅
            item['quote_change'] = td.xpath('./td[5]/text()').extract_first()#  忘了。。你们不用管他
            item['lowest_price'] = td.xpath('./td[6]/text()').extract_first()#最低价
            item['highest_price'] = td.xpath('./td[7]/text()').extract_first()#最高价
            item['volume'] = td.xpath('./td[8]/text()').extract_first()# 成交量
            item['turnover'] = td.xpath('./td[9]/text()').extract_first()#换手量
            item['turnover_rate'] = td.xpath('./td[10]/text()').extract_first()#换手率
            yield item
