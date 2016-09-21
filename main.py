__author__ = 'charan'

'''import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://download.qnap.com/QPKG/img/python_640x400.png")


fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

from urllib import request

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=11&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r"goog.csv"
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)
https://www.facebook.com/kartheek.reddy.35/photos?source_ref=pb_friends_tl
def amazon_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.facebook.com/kartheek.reddy.35/friends?source_ref=pb_friends_tl'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div', {'class': 'fsl fwb fcb'}):
            a = link.string
            print(a)
amazon_spider(1)


import requests
from bs4 import BeautifulSoup


def amazon_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.amazon.in/s/ref=nb_sb_ss_i_5_7?url=search-alias%3Daps&field-keywords=yureka+plus+back+cover&sprefix=yureka+plus+back+cover%2Caps%2C350&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'a-link-normal s-access-detail-page  a-text-normal'}):
            href = link.get('href')
            # title = link.get('title')
            # print(title)
            get_single_item_dat(href)
            page += 1


def get_single_item_dat(item_url):
        source_code = requests.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for item_name in soup.findAll('span', {'id': 'productTitle'}):
            print(item_name.string)
        for link in soup.findAll('a', {"id": 'brand'}):
            print("By" + link.string)


amazon_spider(1)


tuna = int(input("What's your fav number?\n"))
print(tuna)




while True:
    try:
        number = int(input("What's your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make Sure you enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("Loop Complete")



class Enemy:
    life = 3

    def attack(self):
        print('Ouch!!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am Dead')
        else:
            print(str(self.life)+" life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()


class Tuna:

    def __init__(self):
        print('BKlrlrgBlrBLr')

    def swim(self):
        print('I am swimming')

flipper = Tuna()
flipper.swim()
#


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()



class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)



class Parent:

    def  print_last_name(self):
        print('Lelaboyena')


class Child(Parent):

    def print_first_name(self):
        print('Charan')

    def print_last_name(self):
        print('Teja')

Charan = Child()
Charan.print_first_name()
Charan.print_last_name()
x


class Mario():

    def move(self):
        print('I am moving! ')


class Shroom():

    def eat_shroom(self):
        print('Now I amm Big!')


class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()



import threading


class CharansMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = CharansMessenger(name='Send Out messages ')
y = CharansMessenger(name='Receive Messages ')
x.start()
y.start()




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
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+:<>?{}|\[];\"-=`/.,'"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://www.amazon.in/s/ref=nb_sb_ss_i_5_7?url=search-alias%3Daps&field-keywords=yureka+plus+back+cover&sprefix=yureka+plus+back+cover%2Caps%2C350&page=1')



date, name, price = ['December 24, 2016', 'Bread Gloves', '25$']
print(name)
python cookbook



def dro_first_last(grades):
    first, *middle,last = grades
    avg = sum(middle)/len(middle)
    print(avg)

dro_first_last([214, 215, 219215, 21, 2135])


first = ['charan', 'Aruna', 'Dad']
last = ['Lellaboyena', 'L', 'Nana']
names = zip(first, last)

for a, b in names:
    print(a, b)


answer = lambda x: x*7
print(answer(5))

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print(sorted(zip(stocks.values(), stocks.keys())))

from PIL import Image

img = Image.open("charan_py.jpg")
print(img.size)
print(img.format)

img.show()


from PIL import Image

img = Image.open("charan_py.jpg")
area = (200, 0, 2000, 1000)
cropped_img = img.crop(area)


img.show()
cropped_img.show()


from PIL import Image

one = Image.open("1.jpg")
img = Image.open("charan_py.jpg")

area = (0, 0, 480, 359)

img.paste(one, area)
img.show()

from PIL import Image

img = Image.open("charan_py.jpg")
print(img.mode)
r, g, b = img.split()

r.show()
g.show()
b.show()



from PIL import Image

img = Image.open("charan_py.jpg")
r, g, b = img.split()

new_img = Image.merge("RGB", (g, b, r))
new_img.show()


from PIL import Image

img = Image.open("charan_py.jpg")
img1 = Image.open("1.jpg")
area = (0, 0, 480, 359)
cropped_img = img.crop(area)
r1, g1, b1 = cropped_img.split()
r2, g2, b2 = img1.split()

new_img = Image.merge("RGB", (r1, g2, b1))
new_img.show()

from PIL import Image

img = Image.open("charan_py.jpg")
Square_img = img.resize((500, 500))
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = img.transpose(Image.ROTATE_90)
Square_img.show()
flip_img.show()
spin_baby.show()


from PIL import Image

img = Image.open("charan_py.jpg")
black_white = img.convert("L")
black_white.show()

from PIL import Image
from PIL import  ImageFilter

img = Image.open("charan_py.jpg")
blur = img.filter(ImageFilter.GaussianBlur)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()


from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal (b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
original_data = unpack('iif', packed_data)
print(original_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))


income = [10, 30, 75]


def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)



# ---------- Binary AND -----------

a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000
print(c)

# ----------- Binary Right Shift ----

x = 240     # 11110000
y = x >> 2  # 00111100
print(y)



import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'CHARAN', 'price': 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))


stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print(min(stocks))

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)

from collections import Counter

text = "CHARAN Charan charan charan to charan in charan on charan Charan"

words = text.split()
print(words)
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

from operator import itemgetter

users = [
    {'fname': 'AAPL', 'lname': 'L'},
    {'fname': 'Charan', 'lname': 'A'},
    {'fname': 'cherry', 'lname': 'Q'},
    {'fname': 'AAAAp', 'lname': 'Z'},
    {'fname': 'Charan', 'lname': 'L'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-----------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)
'''
from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + ": " + str(self.user_id)

users = [
    User('Charan', 31),
    User('Vgad', 71),
    User('mki', 21),
    User('Asfgt', 51),
    User('Mklo', 61),
    User('Pqwerty', 1)
]

for user in users:
    print(user)

print('-----')
for user in sorted(users, key=attrgetter('name')):
    print(user)

print('-----')
for user in sorted(users, key=attrgetter('user_id')):
    print(user)

'''
import socket

ip = socket.gethostbyname('www.amazon.com')
print(ip)
'''