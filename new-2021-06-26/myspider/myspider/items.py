# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() #教师名称
    title = scrapy.Field() #标题
    desc = scrapy.Field() #


# if __name__ == '__main__':
#     #可以当作字典来用
#     item = MyspiderItem()
#     item['name'] = "giao老师"
#     item['title'] = "我giao"
#     item['desc'] = "西巴"
#     print(item)
