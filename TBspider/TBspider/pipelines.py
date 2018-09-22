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
        with open('./result.txt','w+')as f:
            print('11111111111111111111')
            f.write(json.dumps(item))
        return item
