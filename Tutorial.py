__author__ = 'charan'
'''
print("I hope This Works")
name = "Charan Teja"
foods = ['bacon', 'tuna', 'ham', 'beef']

def function():
    print("This is from function")


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)


def allowed_datin_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age


def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)


a = 7823


def corn():
    a=125
    print(a)


def fudge():
    print(a)


def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)


def dumb_sentence(name="Charan", action='ate', item='tuna'):
    print(name, action, item)


def health_calendar(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)
if name is "Charan":
    print("Hey "+name)
elif name is "Charan Teja1":
    print("Welcome :D :* "+name)
    for f in foods[:3]:
        print(f)
        print(len(f))
elif name is "Charan Teja2":
    print("Welcome :D :* "+name)
    for x in range(5,50,5):
        print(x)
elif name is "Charan Teja3":
    c =5
    while c < 10:
       print(c)
       c +=1
elif name is "Charan Teja4":
    magicNumber = 16
    for n in range(101):
        if n%4 is 0:
            print("Magic Number is ", n)
            break
        else:
            print(n)
elif name is "Charan Teja5":
    magicNumber = 16
    for n in range(101):
        if n%4 is 0:
            print(n)
elif name is "Charan Teja6":
    numbersTaken = [1, 5, 18, 13, 25]

    print("Here are the numbers that are stil available:")
    for n in range(1,31):
        if n in numbersTaken:
            continue
        print(n)
elif name is "Charan Teja7":
    function()
    bitcoin_to_usd(12.1)
    print(allowed_datin_age(23),"is your girls min agee")
    get_gender('m')
    corn()
    fudge()
    dumb_sentence()
    dumb_sentence("Kartheek", "farts", "gently")
    dumb_sentence(item='awesome')
    dumb_sentence(item='awesome', action='is')
    add_numbers(3)
    add_numbers(3, .3, 2000.6)
    add_numbers(3, 2, 1000)
    charan_data=[27, 20, 0]
    # health_calendar(charan_data[0], charan_data[1], charan_data[2])
    health_calendar(*charan_data)
elif name is "Charan Teja":

else:
    print("Hey your not "+name)


groceries = {'cereal', 'milk', 'egg', 'beer', 'duct tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
    print("you already have milk boss")
else:
    print("oh, yeah you need milk")


classmates = {'Tony': ' Cool but smells', 'Charan': ' Awesome Dude', 'Lucy': ' Too many questions'}
print(classmates)
print(classmates['Charan'])
for k, v in classmates.items():
    print(k + v)

import tuna
import random

tuna.fish()

x = random.randrange(1, 1000)
print(x)'''