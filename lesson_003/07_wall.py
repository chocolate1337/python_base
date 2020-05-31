# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич


delta = 0
for y in range(0, 650, 50):
    delta += 50
    for x in range(delta, 650, 100):
        point = sd.Point(x, y)
        point1 = sd.Point(x + 100, y + 50)
        sd.rectangle(point, point1, sd.COLOR_ORANGE, 2)
    delta -= 100

sd.pause()

