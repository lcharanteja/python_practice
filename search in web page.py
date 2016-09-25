__author__ = 'charan'

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'a-link-normal s-access-detail-page  a-text-normal'}):
        content = post_text.string
        # print(content)
        words = content.lower().split()
        #print(words)
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
        #print("word list")
        #print(word_list)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+:<>?{}|\[];\"-=`/.,'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            #print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    #print(word_count)
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://www.amazon.in/s/ref=nb_sb_ss_i_5_7?url=search-alias%3Daps&field-keywords=yureka+plus+back+cover&sprefix=yureka+plus+back+cover%2Caps%2C350&page=1')
