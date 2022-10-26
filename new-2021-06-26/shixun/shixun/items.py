# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixunItem(scrapy.Item):
    # define the fields for your item here like:
    # 股票名称
    name = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 开盘价
    opening_price = scrapy.Field()
    # 收盘价
    closing_price = scrapy.Field()
    # 涨跌额
    ups_and_downs = scrapy.Field()
    # 涨跌幅(%)
    quote_change = scrapy.Field()
    # 最低价
    lowest_price = scrapy.Field()
    # 最高价
    highest_price = scrapy.Field()
    # 成交量(手)
    volume = scrapy.Field()
    # 成交金额(万元)
    turnover = scrapy.Field()
    # 振幅( %)
    amplitude = scrapy.Field()
    # 换手率(%)
    turnover_rate = scrapy.Field()


class SouHuItem(scrapy.Item):
    # define the fields for your item here like:
    # 股票名称
    name = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 开盘价
    opening_price = scrapy.Field()
    # 收盘价
    closing_price = scrapy.Field()
    # 涨跌额
    ups_and_downs = scrapy.Field()
    # 涨跌幅(%)
    quote_change = scrapy.Field()
    # 最低价
    lowest_price = scrapy.Field()
    # 最高价
    highest_price = scrapy.Field()
    # 成交量(手)
    volume = scrapy.Field()
    # 成交金额(万元)
    turnover = scrapy.Field()
    # 换手率(%)
    turnover_rate = scrapy.Field()
