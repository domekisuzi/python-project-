import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# cralspider经常应用于数据在一个页面上进行采集的情况,如果在数据在多个页面上,这个时候通常使用spider,meta等
class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    # 连接提取规则
    rules = (
        #使用Rule类生成连接提取规则
        #允许域,接受正则表达式
        #follow参数决定是否在链接提取器提取的链接对应的响应中继续应用链接提取器提取链接
        #设置详情提取规则
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        #设置翻页提取规则,无需解析
        Rule(LinkExtractor(allow=r'Items/'), follow = True)
    )
    #在crawlspider中不能重写parse方法
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
