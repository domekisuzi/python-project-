import scrapy


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login/']

    def parse(self, response):
        # 从登录页面响应中解析出post数据
        # 针对登录url发送post请求
        #注意登陆时,别用邮箱,用用户名!!
        token = response.xpath('//*[@id="login"]/div[4]/form/input[1]/@value').extract_first()
        str = ''' commit: Sign in
                 login: domekisuzi
                 password: suzi123456.
                 webauthn-support: supported'''
        post_data = {x.split(': ')[0].strip(): x.split(': ')[-1].strip() for x in str.split('\n')}
        post_data['authenticity_token'] = token
        print(post_data)
        yield scrapy.FormRequest(url="https://github.com/session", callback=self.after_login, formdata=post_data)

    def after_login(self, response):
        yield scrapy.Request('https://github.com/domekisuzi', callback=self.check_login)

    def check_login(self, response):
        print("----------"+response.xpath('/html/head/title/text()').extract_first())

