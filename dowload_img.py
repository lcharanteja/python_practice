__author__ = 'charan'

import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://download.qnap.com/QPKG/img/python_640x400.png")