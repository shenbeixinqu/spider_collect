import requests
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_random_ua():
	ua = UserAgent()
	return ua.random

headers = {
	'User-Agent': get_random_ua()
}

url = "https://www.dailiproxy.com/cn-free/free-liaoning-ip/"
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
selector = etree.HTML(res.text)
xpath_reg = "//table/table/tbody/tr/td[0]/text()"
results = selector.xpath(xpath_reg)
content = results[0]
print("content",content)
