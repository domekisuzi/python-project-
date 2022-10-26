# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#数据处理,清理保存
import  json


class MyspiderPipeline:

    def __init__(self):
        self.file = open('itcast.json','w')
    def process_item(self, item, spider):
        #y由于item不是字典类,需要将item进行强转,该操作只能在scrapy中进行
        item = dict(item)
        print('item:',item)
        json_data = json.dumps(item,ensure_ascii=False)+',\n'
        self.file.write(json_data)
        #默认使用完管道后需要将数据返回给引擎
        return item
    def __del__(self):
        self.file.close()