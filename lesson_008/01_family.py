# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


from termcolor import cprint
from random import randint


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        return 'В доме денег осталось {}, еды {}, грязь {}'.format(
            self.money, self.food, self.dirt)


class Mans:
    food = 0

    def __init__(self, name, home):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def eat(self):
        if self.house.food > 0:
            # TODO может быть тебе в if-е только вычислять, сколько еды будет съедено, а все остальное вне if-а через переменную, 
            #  потому, что тут идет дублирование кода
            if self.house.food > 60:
                cprint('{} поел'.format(self.name), color='yellow')
                self.fullness += 30
                self.house.food -= 30
                Mans.food += 30
            else:
                need_food = abs(self.fullness - 30)
                self.fullness += need_food
                self.house.food -= need_food
                Mans.food += need_food
                cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            # TODO тут молодец
            self.fullness -= 10

    def act(self):
        self.house.dirt += 5 / 2
        if self.fullness <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 20:
            self.eat()
            return False
        return True # TODO то есть true - если не было действия, тогда если умер - тоже надо возвращать false

    def __str__(self):
        return '{}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)


class Husband(Mans):
    money = 0
    # TODO не надо переопределять метод, если ты в нем только вызываешь супер. home надо передавать в параметрах тут или сделать метод go_to_home отдельный
    def __init__(self, name):
        super().__init__(name=name, home=home)
    # TODO этот метод тоже не надо переопределять.
    def __str__(self):
        return super().__str__()

    def act(self):
        # TODO тут можно уменьшить вложенность, типа если акт был, то сразу ретурн, а потом уже все остальные условия.
        if super().act():
            if self.house.money < 150:
                self.work()
            elif self.happiness < 20:
                self.gaming()
            else:
                self.work()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10
        Husband.money += 150

    def gaming(self):
        cprint('{} играл в WoT целый день'.format(self.name), color='green')
        self.happiness += 20
        self.fullness -= 10


class Wife(Mans):
    coat = 0

    def __init__(self, name):
        super().__init__(name=name, home=home)

    def __str__(self):
        return super().__str__()

    def act(self):
         # TODO тут тоже можно уменьшить вложенность
        if super().act():
            if self.house.food <= 60:
                self.shopping()
            elif self.happiness <= 20:
                self.buy_fur_coat()
            elif self.house.dirt > 90:
                self.clean_house()
            else:
                self.shopping()

    def shopping(self):
        if self.house.money >= 100:
            # TODO тут тоже вынеси общие строки за if
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 60
            self.house.food += 60
            self.fullness -= 10
        elif self.house.money <= 50:
            self.house.money -= 20
            self.house.food += 20
            self.fullness -= 10
        else:
            cprint('{} хотела купить еды, но дома нет денег'.format(self.name), color='red')
            self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money > 350:
            cprint('{} сходила в магазин и купила шубу!'.format(self.name), color='magenta')
            self.happiness += 60
            self.house.money -= 350
            self.fullness -= 10
            Wife.coat += 1
        else:
            cprint('{} пыталась купить шубу, но не хватает денег!'.format(self.name), color='red')
            self.fullness -= 10

    def clean_house(self):
        cprint('{} убиралась весь день!'.format(self.name), color='magenta')
        self.house.dirt = 0
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(1, 366, 1):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    if day == 365:
        cprint(f'Итоги года: Всего денег заработано - {Husband.money}, '
               f'Съедено еды - {Mans.food}, Куплено шуб - {Wife.coat}', color='green')




######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
