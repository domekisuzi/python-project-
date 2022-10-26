# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from pymongo import MongoClient


#可以存HDFS里面
# 用于数据存储
class WanyiPipeline:
    def open_spider(self, spider):
        if spider == 'job':
            self.file = open('wangyi.json', 'w')

    def process_item(self, item, spider):
        if spider == 'job':
            item = dict(item)
            str_data = json.dumps(item, ensure_ascii=False) + ",\n"
            self.file.write(str_data)
            # print('-------------')
            # print('我在pipe中')
            # print('-------------')
            return item


    def close_spider(self, spider):
        if spider == 'job':
            self.file.close()

class WangyiSimplePipeline:
    def open_spider(self, spider):
        if spider == 'job_sample':
            self.file = open('wangyi_sample.json', 'w')

    def process_item(self, item, spider):
        if spider == 'job_sample':
            item = dict(item)
            str_data = json.dumps(item, ensure_ascii=False) + ",\n"
            self.file.write(str_data)
            # print('-------------')
            # print('我在pipe中')
            # print('-------------')
            return item

    def close_spider(self, spider):
        if spider == 'job_sample':
            self.file.close()


class MongoPipeline(object):
    def open_spider(self, spider):
            self.client = MongoClient('127.0.0.1', 27017)
            self.db = self.client['itcast']
            self.col = self.db['wangyi']


    def process_item(self, item, spider):
            data = dict(item)
            self.col.inset(data)
            return item

    def close_spider(self, spider):
            self.client.close()

