# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# useful for handling different item types with a single interface

import base64
from scrapy.http import HtmlResponse
from shixun import util
from fake_useragent import UserAgent
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shixun.log import logger
import redis
from shixun.settings import USER_AGENT


class RandomProxy(object):
    def __init__(self):
        s = open('proxy.json', 'r')
        self.proxies = []
        while True:
            line = s.readline().replace('\n', '')
            if line:
                self.proxies.append(line)
            else:
                break
        logger.warn('调用了一次读文件')

    def process_request(self, request, spider):
        proxy = random.choice(self.proxies)
        print('当前代理为:' + proxy)
        request.meta['proxy'] = str(proxy)
        print("当前代理为" + request.meta['proxy'])
        print("meta为" + str(request.meta))
        print("request为" + request.url)


class RandomUserAgent(object):
    def process_request(self, request, spider):
        # print(request.headers['User-Agent'])
        fake = UserAgent()
        ua = fake.random
        request.headers['User-Agent'] = ua


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        if request.meta['flag']:
            url = request.url
            options = Options()
            options.add_argument("--disable-blink-features")
            options.add_argument("--disable-blink-features=AutomationControlled")
            #设置不弹出浏览器
            options.add_argument('headless')
            # options.add_argument('--headless')
            # options.add_argument('user-agent=' + USER_AGENT)
            driver = webdriver.Chrome(
                executable_path="E:\\python_project\\new-2021-06-26\\shixun\\shixun\\chromedriver.exe", options=options)
            driver.get(url=url)
            driver.implicitly_wait(2)
            logger.warning("Selenium,当前解析的是: " + request.url)
            data = driver.page_source
            logger.warning("Selenium解析完成")
            # driver.close()
            time.sleep(2)
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            driver.close()
            # 返回响应
            return res
