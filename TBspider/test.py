import re
import requests
url = 'http://127.0.0.1:5000/random'

proxy = requests.get(url).text
print(proxy)