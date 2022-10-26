import scrapy


class GitSpider(scrapy.Spider):
    name = 'GitSpider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/']

    # 由于开启start_url的 start_requests方法没有自带cookie,因此想要模拟登录必须开启重写该方法
    def start_requests(self):
        url = self.start_urls[0]
        temp = '_octo=GH1.1.268124366.1644215472; _device_id=8b7bc864846650974be18a1da466df05; ' \
               'user_session=MB_-_vRMLTBCmfCvKkWU516ooX_V0OVjHMlfcZgs2FgY1MhO; ' \
               '__Host-user_session_same_site=MB_-_vRMLTBCmfCvKkWU516ooX_V0OVjHMlfcZgs2FgY1MhO; logged_in=yes; ' \
               'dotcom_user=domekisuzi; color_mode={"color_mode":"auto","light_theme":{"name":"dark_high_contrast",' \
               '"color_mode":"dark"},"dark_theme":{"name":"dark_high_contrast","color_mode":"dark"}}; ' \
               'tz=Asia/Shanghai; _gh_sess=OkIwtDiw2gU1bwJDxVN2NyrNp2adSfNpUkrcbQXCe6/Vr3Esy7HMCV9Z79/KCO' \
               '+/Ia0Y9vCq0oR2EniCvuo/1sLFcr4vwIsQGl0hRuh22wj6zbTdK9qElf31B7vSBaQz3q/Hplntz6ZWPC5RTM' \
               '+qXOUFuUhqnwkBfXsJL2WCS/3r28taLdYN4JRauFjosFKJ--4pTqnylWlm/ojRid--/1VaYeVqGZcop2HfOAjeUg== '
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')}
        print(cookies)
        yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
