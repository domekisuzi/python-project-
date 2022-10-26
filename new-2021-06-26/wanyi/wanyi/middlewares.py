# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import time
from selenium import webdriver
from  selenium.webdriver.chrome.options import Options

from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        # if request.meta['flag']:
            url = request.url
            options = Options()
            options.add_argument("--disable-blink-features")
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(executable_path="E:\\python_project\\new-2021-06-26\\shixun\\shixun\\chromedriver.exe",options=options)
            driver.get(url=url)
            # logger.warning("Selenium,当前解析的是: "+request.url)
            time.sleep(2)
            data = driver.page_source
            # logger.warning("Selenium解析完成")
            # driver.close()
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            #返回响应
            return res
