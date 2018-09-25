# -*- coding: utf-8 -*-
# /usr/bin/env python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from TBspider.items import TbspiderItem


class TbspiderPipeline(object):
    def process_item(self, item, spider):
        for one in item['items']:  # read every item in the page
            pass  # 这里需要重组数据然后写入数据库
        return item
