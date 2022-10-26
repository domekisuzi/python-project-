import scrapy
from shixun.items import ShixunItem
from shixun.log import logger


class StockGetSpider(scrapy.Spider):
    name = 'stock_get'
    # allowed_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/0601857.html#3a01']

    # def start_requests(self):
    #     logger.warning("开启使用爬虫")
    #     url = self.start_urls[0]
    #     # 先经过中间件,然后交给下载器
    #     yield scrapy.Request(url=url, callback=self.parse, meta={'flag': True})
    def __init__(self):
        self.stock_url = []
    def parse(self, response):
        # 热门url
        logger.warning('parse解析的url为'+response.url)
        stoke_url = response.xpath('//a[@class="cDBlue"]/@href').extract()
        logger.critical("stoke_url列表为" + str(stoke_url))
        for url in stoke_url[1:1:]:
            logger.warning("进入parse阶段,当前parse的url为" + url)
            # 下载器将响应还给爬虫,爬虫经过中间件进入下载器
            yield scrapy.Request(url=url, callback=self.parse_page,
                                 meta={'flag': True}, dont_filter=True, errback=self.errback)

    def errback(self, failure):
        logger.critical(repr(failure))

    def parse_page(self, response):
        href = response.urljoin(response.xpath(
            '//div[@class="sub_menu tab_panel clearfix"][1]/ul/li[@class=""][6]/a/@href').extract_first())
        logger.warning("进入打开历史交易数据阶段,当前url为" + href)
        # 历史交易数据url,可以直接去请求
        yield scrapy.Request(url=href, callback=self.parse_data, meta={'flag': False})
    def parse_data(self, response):
        logger.warning('--------------')
        logger.warning('prase_data的网址为'+response.url)
        trs = response.xpath('//*[@class="table_bg001 border_box limit_sale"]//tbody/tr')
        logger.critical("trs为"+trs)
        for td in trs:
            item = ShixunItem()
            item['name'] = td.xpath('/html/body/div[2]/h1/span/text()').extract_first()
            item['date'] = td.xpath('./td[1]/text()').extract_first()
            item['opening_price'] = td.xpath('./td[1]/text()').extract_first()
            item['highest_price'] = td.xpath('./td[2]/text()').extract_first()
            item['lowest_price'] = td.xpath('./td[3]/text()').extract_first()
            item['closing_price'] = td.xpath('./td[4]/text()').extract_first()
            item['ups_and_downs'] = td.xpath('./td[5]/text()').extract_first()
            item['quote_change'] = td.xpath('./td[6]/text()').extract_first()
            item['volume'] = td.xpath('./td[7]/text()').extract_first()
            item['turnover'] = td.xpath('./td[8]/text()').extract_first()
            item['amplitude'] = td.xpath('./td[9]/text()').extract_first()
            item['turnover_rate'] = td.xpath('./td[10]/text()').extract_first()
            yield item

        # start_urls = ['https://movie.douban.com/subject_search?search_text='+'宁浩'+'&cat=1002&start=']
# def start_requests(self):
#     url = self.start_urls[0]
#     temp = '''_ntes_nnid=bea5c857a8576a9373567196f2d7c4cb,1644064684928; _ntes_nuid=bea5c857a8576a9373567196f2d7c4cb; nts_mail_user=domekisuzi@163.com:-1:1; NTES_PASSPORT=.hFym_MFpZ.bHzjfh0a4bVuVN_CQKGSidkO5qin1_lm9YtclYUOmhkSXw1AHoqhIg38aCTcpqKSO4UsadDmHw_kR.e1gl3_niMP7BpzEM3adwCivpGe2k7HmNFVz7jr2RKC_RMHi7Xh.d.czkrW5BMW2amJ7mzgOTeiMQuu.cghfZy4pghqgckmzy7CAZeHQY; P_INFO=domekisuzi@163.com|1654324075|1|mail163|00&99|hun&1652803264&mail163#hun&430100#10#0#0|&0||domekisuzi@163.com; _antanalysis_s_id=1654739401063; _antanalysis_s_id=1654739809231; _ntes_stock_recent_=1002230|0601857; _ntes_stock_recent_=1002230|0601857; _ntes_stock_recent_=1002230|0601857; s_n_f_l_n3=74cd2a7a270459f31654756496012; ne_analysis_trace_id=1654756803443; ariaDefaultTheme=undefined; cm_newmsg=user=domekisuzi@163.com&new=-1&total=-1; vinfo_n_f_l_n3=74cd2a7a270459f3.1.1.1654739423925.1654747148088.1654756836367'''
#     cookies = {data.split('=')[0].strip():data.split('=')[-1].strip() for data in temp.split('; ')}
#     print(cookies)
#     yield  scrapy.Request(url=url,callback=self.parse,cookies=cookies)

