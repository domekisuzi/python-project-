# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
from scrapy import signals
from fake_useragent import UserAgent
from Douban.settings import PROXY_LIST
import base64

fake = UserAgent()


class RandomUserAgent(object):
    def process_request(self, request, spider):
        # print(request.headers['User-Agent'])
        ua = fake.random
        request.headers['User-Agent'] = ua


# 如果有账号密码需要认证,网上搜索,http认证,基本认证,摘要认证
class RandomProxy(object):
    def process_request(self, request, spider):

        proxy = random.choice(PROXY_LIST)
        if 'user_passwd' in proxy:
            # 对账号密码进行编码
            b64_up = base64.b64encode(proxy['user_passwd'].encode())
            # 设置认证,必须加空格
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
            # 设置代理
            request.meta['proxy'] = str(proxy['ip_port'])
        else:
            # 设置代理,不加http://会报错
            request.meta['proxy'] = "http://" + proxy['ip_port']
        print("当前代理为" + request.meta['proxy'])
