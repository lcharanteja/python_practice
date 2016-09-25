__author__ = 'charan'

import requests
from bs4 import BeautifulSoup


def amazon_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.amazon.in/s/ref=nb_sb_ss_i_5_7?url=search-alias%3Daps&field-keywords=yureka+plus+back+cover&sprefix=yureka+plus+back+cover%2Caps%2C350&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'a-link-normal s-access-detail-page  a-text-normal'}):
            href = link.get('href')
            # title = link.get('title')
            # print(title)
            get_single_item_dat(href)
            page += 1


def get_single_item_dat(item_url):
        source_code = requests.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for item_name in soup.findAll('span', {'id': 'productTitle'}):
            print(item_name.string)
        for link in soup.findAll('a', {"id": 'brand'}):
            print("By" + link.string)


amazon_spider(1)
