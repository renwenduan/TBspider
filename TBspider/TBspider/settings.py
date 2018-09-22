# -*- coding: utf-8 -*-

# Scrapy settings for TBspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TBspider'

SPIDER_MODULES = ['TBspider.spiders']
NEWSPIDER_MODULE = 'TBspider.spiders'
# COOKIES=['hng=CN%7Czh-CN%7CCNY%7C156; t=1d70267cc716ede038297ce56a920d34; _tb_token_=5d3e6e363beb7; cookie2=1af5be81509b911cdf22fa98285e7a71; cna=acPDE+JU9xECAd5EH3Go29C9; _m_h5_tk=8210c6ad3689bd049777822ce72ccb32_1537595596719; _m_h5_tk_enc=434cdd83db4967309244f5cf4032e2a3; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=UtASsssmfaCOMId3WwGQmg%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=true&pas=0&cookie14=UoTfLJBB8ANl5A%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByRuXL7mOuApMzyg%3D&id2=VyyX5kmmMHv5&nk2=1TOymB2XNQ%3D%3D&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu6BB5%5Cu4EFB%5Cu65871; _l_g_=Ug%3D%3D; ck1=""; unb=406070892; lgc=%5Cu6BB5%5Cu4EFB%5Cu65871; cookie1=VymaOUaVRuFPhOhlk52qSXoIp0ao4%2BcUEKeM3Dma8kg%3D; login=true; cookie17=VyyX5kmmMHv5; _nk_=%5Cu6BB5%5Cu4EFB%5Cu65871; uss=""; csg=f7ab2067; skt=17303e28dde104e0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; whl=-1%260%260%260; isg=BMHBPatkfrV0XZKBPD_vN33p0AQbRjTmF01LoyMWvUgnCuHcaz5FsO8M6HhMAs0Y']
# referers='https://dxcyt.m.tmall.com/shop/shop_auction_search.htm?spm=a1z60.7754813.0.0.70844f37loqjNl&suid=3715986608&sort=default'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Mobile Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': '*/*',
#   'accept-encoding':'gzip, deflate, br',
#   'Accept-Language': 'zh-CN,zh;q=0.9',
  # 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Mobile Safari/537.36',
  # 'cookie':COOKIES[0],
  # 'refer':referers,
  # ':path':'/shop/shop_auction_search.do?&suid=3715986608&sort=s&p=1&page_size=12&from=h5&shop_id=409787848&ajson=1&_tm_source=tmallsearch&callback=jsonp_17624162',
  # ':authority':'dxcyt.m.tmall.com'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'TBspider.middlewares.TbspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'TBspider.middlewares.TbspiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'TBspider.pipelines.TbspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# REDIRECT_ENABLED = True
dont_filter=True