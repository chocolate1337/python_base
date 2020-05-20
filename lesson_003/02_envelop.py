# -*- coding: utf-8 -*-
import random

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта,
# если размеры равны - лист входит в конверт впритирку)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

# т.к вставляем в условии паралельно то достаточно посчитать площадь конверта и листа и сравнить

S_envelop = envelop_x * envelop_y
if S_envelop >= (paper_x * paper_y):
    print('ДА')
else:
    print('НЕТ')
# TODO здесь ваш код

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)


# т.к по условию грани опять паралельны то достаточно представить что кирпич не объемный и сравнивать две площади
# сделал с рандомом наглядно всё видно


# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

hole_x, hole_y = 8, 9
s_hole = hole_x * hole_y  # площадь дыры
cnt = 0
while cnt <= 10:
    cnt += 1
    brick_x = random.randint(1, 20)
    brick_y = random.randint(1, 20)
    brick_z = random.randint(1, 20)
    if (s_hole >= brick_x * brick_y) or (s_hole >= brick_x * brick_z) or (s_hole >= brick_y * brick_z):
        print('Влезет')
        print(brick_x, brick_y, brick_z, '- ВЛЕЗАЕТ ПРИ ТАКИХ ЗНАЧЕНИЯХ', '\n')
    else:
        print('Не влезет')
        print(brick_x, brick_y, brick_z, '- НИКАК ПРИ ТАКИХ ЗНАЧЕНИЯХ \n')
