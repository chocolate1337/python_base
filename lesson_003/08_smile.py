# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, colors):
    sd.circle(sd.Point(x + 11, y + 11), 6, colors, 1)
    sd.circle(sd.Point(x - 9, y + 11), 6, colors, 1)
    sd.circle(sd.Point(x, y), 30, colors, 1)
    sd.line(sd.Point(x - 6, y - 9), sd.Point(x + 7, y - 9), colors, 1)
    sd.line(sd.Point(x - 6, y - 9), sd.Point(x - 9, y - 6), colors, 1)
    sd.line(sd.Point(x + 7, y - 9), sd.Point(x + 10, y - 6), colors, 1)


for i in range(10):
    x = random.randint(100, 600)
    y = random.randint(100, 600)
    smile(x, y, sd.COLOR_WHITE)

sd.pause()

# зачет!
