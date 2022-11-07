import scrapy
from shixun.items import ShixunItem


class DetailGetSpider(scrapy.Spider):
    name = 'detail_get'
    allowed_domains = ['163.com']
    start_urls = ['http://http://quotes.money.163.com/trade/lsjysj_002230.html/']

    def start_requests(self):
        cookie_data = '''_ntes_nnid=bea5c857a8576a9373567196f2d7c4cb,1644064684928;
         _ntes_nuid=bea5c857a8576a9373567196f2d7c4cb;
         nts_mail_user=domekisuzi@163.com:-1:1;
          NTES_PASSPORT=.hFym_MFpZ.bHzjfh0a4bVuVN_CQKGSidkO5qin1_lm9YtclYUOmhkSXw1AHoqhIg38aCTcpqKSO4UsadDmHw_kR.e1gl3_niMP7BpzEM3adwCivpGe2k7HmNFVz7jr2RKC_RMHi7Xh.d.czkrW5BMW2amJ7mzgOTeiMQuu.cghfZy4pghqgckmzy7CAZeHQY; P_INFO=domekisuzi@163.com|1654324075|1|mail163|00&99|hun&1652803264&mail163#hun&430100#10#0#0|&0||domekisuzi@163.com;
           _ntes_stock_recent_plate_=|hy003012:石油加工; vjuids=82fb38f3.18152537365.0.d5403d8eaa437;
            vjlast=1654943610.1654943610.30;
             _antanalysis_s_id=1655001672862;
              _ntes_stock_recent_=0601939|1000009|0601857|1002230; _ntes_stock_recent_=0601939|1000009|0601857|1002230; 
              _ntes_stock_recent_=0601939|1000009|0601857|1002230; 
              NTES_SESS=amOwRmSwJEX4ni2p3rgUjNk2wQwj6xj1n7k1_uKOZz9QAZ_WA7Kw6gFBVptk9y6XrvYSTdAWTeK..ZWYTryihHvSOc5N1Uxw45k28.90_oyg3mcqNq9yBmtzaUm37PuPWNoKCfsXbDRS8ZGFCmRFwtqJ_OAepyN1IONbnqQpb6cd5aanTLPRUWAsel_1.tX0Ue1ENeBTJ5JYg; S_INFO=1655025056|1|0&60##|domekisuzi; ANTICSRF=5122e32fdd00173fd5ab49ca3145469d; 
              s_n_f_l_n3=74cd2a7a270459f31655051067817; ne_analysis_trace_id=1655051242778; cm_newmsg=user=domekisuzi@163.com&new=7&total=45; 
              _antanalysis_s_id=1655054462734; ariaDefaultTheme=undefined; vinfo_n_f_l_n3=74cd2a7a270459f3.1.17.1654739423925.1655048269241.1655054566158'''
        cookies = {x.split('=')[0].strip(): x.split('=')[-1].strip() for x in cookie_data.strip('; ')}
        yield scrapy.Request(url=self.start_urls[0], cookies=cookies, callback=self.parse)

    def parse(self, response):
        tr = response.xpath('/html/body/div[2]/div[4]/table/tbody/tr')
        for td in tr:

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
            print(item)
            yield item