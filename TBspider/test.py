import re
import requests
url = 'http://store.m.tmall.com/shop/shop_auction_search.do?spm=a1z60.7754813.0.0.70844f37loqjNl&suid=3715986608&sort=s&p=1&page_size=12&from=h5&shop_id=409787848&ajson=1'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
html = requests.get(url=url,headers=headers).text
print(html)