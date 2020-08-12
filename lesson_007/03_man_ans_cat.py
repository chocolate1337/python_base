# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def clean_up(self):
        cprint('{} убирался целый день'.format(self.name), color='green')
        self.fullness -= 20
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой себе и коту'.format(self.name), color='magenta')
            self.house.money -= 100
            self.house.food += 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')
    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.money <= 50:
            self.work()
        elif self.fullness <= 20:
            self.eat()
        elif self.house.food <= 20 or self.house.cat_food <= 20:
            self.shopping()
        elif self.house.dirt > 100:
            self.clean_up()


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
    def take_cat_in_to_the_house(self, house):
        self.house = house
        cprint('Человек взял кота и назвал его: {}'.format(self.name), color='cyan')
    def sleep(self):
        cprint('{} спал целый день'.format(self.name), color='green')
        self.fullness -= 10
    def tear_up(self):
        cprint('{} драл обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5
    def act(self):
        if self.fullness <= 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.dirt >150:
            cprint('{} сбежал из дома, в доме очень грязно!...'.format(self.name), color='red')
        dice = randint(1,3)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.tear_up()
        else:
            self.sleep()
class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, Кошачей еды {}, денег осталось {}, грязь {}'.format(
            self.food,self.cat_food, self.money, self.dirt)

my_house = House()

me = Man(name='Влад')
cats = [Cat(name='Кроша'),
        Cat(name='Масяня'),
        Cat(name='Жора')]
# У родителей дома 3 кота, это в честь них я дал им имена)

me.go_to_the_house(house=my_house)
for cat in cats:
    cat.take_cat_in_to_the_house(house=my_house)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    me.act()
    for cat in cats:
        cat.act()

    print('--- в конце дня ---')
    print(me)
    for cat in cats:
        print(cat)
    print(my_house)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
