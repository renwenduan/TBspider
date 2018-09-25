# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class TbspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shop_id = Field()
    user_id = Field()
    shop_title = Field()
    total_page =Field()
    shop_Url = Field()
    items = Field()
    # item_id =Field()
    # title =Field()
    # img = Field()
    # sold =Field()
    # quantity = Field()
    # totalSoldQuant = Field()
    # price = Field()
    # item = {'item_id':item_id,'title':title,'img':img,'sold':sold,'quantity':quantity,'totalSoldQuant':totalSoldQuant,'price':price}