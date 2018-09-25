# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,spider
import requests
from urllib.request import quote
import re
import json
import requests
from TBspider.items import TbspiderItem
class TbspiderSpider(scrapy.Spider):
    name = 'tbspider'
    allowed_domains = []
    start_url = 'http://store.m.tmall.com/shop/shop_auction_search.do?spm=a1z60.7754813.0.0.70844f37loqjNl&suid=3715986608&sort=s&p=1&page_size=12&from=h5&shop_id=409787848&ajson=1'

    def start_requests(self):
        proxy = requests.get('http://127.0.0.1:5000/random').text  # fetch the proxy form pool
        random_proxy = 'http://{}'.format(proxy)
        random_proxy = None
        yield Request(self.start_url,callback=self.content_parser,dont_filter=True,meta={'proxy':random_proxy})  # don't filter will be need because of the redirect issue


    def content_parser(self,response):
        doc = response.text   # result byte type can be transfer to json
        format_cont = json.loads(doc)  # load to json

        item = TbspiderItem()
        for field in item.fields:
            if field in format_cont.keys() and len(format_cont['items']) != 0:
                item[field] = format_cont[field]

        yield item