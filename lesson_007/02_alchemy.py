# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __add__(self, other):
        if isinstance(other,Earth):
            return Water_Elemental()
    def __str__(self):
        return 'Шторм. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)
class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)
class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __add__(self, other):
        if isinstance(other,Fire):
            return Rock_Elemental()

    def __str__(self):
        return 'Грязь. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)
class Light:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __add__(self, other):
        if isinstance(other,Earth):
            return Fire_Elemental()
    def __str__(self):
        return 'Молния. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)
class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль. Состоит из ' + str(self.part1) + ' и ' + str(self.part2)


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава. Состит из ' + str(self.part1) + ' и ' + str(self.part2)
class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=Water(),part2=Fire())
        elif isinstance(other, Earth):
            return Dirt(part1=Water(),part2=Earth())



class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava(part1=self, part2=other)

class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust(part1 = self, part2 = other)

        elif isinstance(other, Fire):
            return Light(part1=self, part2=other)
class Earth:
    def __str__(self):
        return 'Земля'
class Rock_Elemental:
    def __str__(self):
        return f'Я Каменный элементаль. Состою из: {Water()}, {Earth()}, {Fire()}'
class Water_Elemental:
    def __str__(self):
        return  f'Я Водяной элементаль. Состою из: {Water()}, {Air()}, {Earth()}'
class Fire_Elemental:
    def __str__(self):
        return f'Я Огненный элементаль. Состою из: {Air()}, {Earth()}, {Fire()}'


#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#   Вода + Земля + Огонь = Каменный элементаль:)
#   Вода + Воздух + Земля = Водяной элементаль
#   Воздух + Огонь + Земля = Огненный элементаль
print(Water()+Earth())
print(Water() + Air())
print(Water() + Fire())
print(Water() + Earth())
print(Air() + Fire())
print(Air() + Earth())
print(Fire() + Earth())
print(Water() + Earth() + Fire())
print(Water() + Air() + Earth())
print(Air() + Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
