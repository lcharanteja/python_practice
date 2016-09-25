__author__ = 'charan'


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

    def print_last_name(self):
        print('Lelaboyena')


class Child(Parent):

    def print_first_name(self):
        print('Charan')

    def print_last_name(self):
        print('Teja')

Charan = Child()
Charan.print_first_name()
Charan.print_last_name()


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
