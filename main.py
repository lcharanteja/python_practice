__author__ = 'charan'

'''
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


import threading


class CharansMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = CharansMessenger(name='Send Out messages ')
y = CharansMessenger(name='Receive Messages ')
x.start()
y.start()







date, name, price = ['December 24, 2016', 'Bread Gloves', '25$']
print(name)

#python cookbook



def dro_first_last(grades):
    first, *middle,last = grades
    avg = sum(middle)/len(middle)
    print(avg)

dro_first_last([214, 215, 219215, 21, 2135])


first = ['charan', 'Aruna', 'Dad']
last = [1, 'L', 'Nana']
names = zip(first, last)
print(list(names))
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

income = [10, 30, 75]


def double_money(dollars):
    return dollars * 2

new_income = list(map(double_money, income))
print(new_income)


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

from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __str__(self):
        return self.name + ": " + str(self.user_id)

    def __repr__(self):
        return self.name + "--> " + str(self.user_id)
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

ip = socket.gethostbyname('www.google.com')
print(ip)
