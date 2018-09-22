# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,spider
import requests
from urllib.request import quote
import re
import json
from TBspider.items import TbspiderItem
class TbspiderSpider(scrapy.Spider):
    name = 'tbspider'
    allowed_domains = []
    start_url = 'http://store.m.tmall.com/shop/shop_auction_search.do?spm=a1z60.7754813.0.0.70844f37loqjNl&suid=3715986608&sort=s&p=1&page_size=12&from=h5&shop_id=409787848&ajson=1'

    def start_requests(self):
        yield Request(self.start_url,callback=self.content_parser,dont_filter=True)  # don't filter will be need because of the redirect issue


    def content_parser(self,response):
        doc = response.text   # result

        print(doc)
        # pt = r"jsonp_.*\((.*})"
        # pattren = re.compile(pt)  # pattern
        # content = pattren.search(doc).groups()[0] # select the content we need
        # print(content,11111)
        content = doc.split('(')[1]
        # print(content)
        format_cont = json.loads(content)  # load to json
        item = TbspiderItem()
        # print(item)
        for field in item.fields:
            if field in format_cont.keys():
                item[field] = format_cont.get[field]
        yield item