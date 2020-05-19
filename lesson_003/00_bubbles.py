# -*- coding: utf-8 -*-
import random

import simple_draw as sd
from simple_draw import circle, Point

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO Уважаемый преподаватель код закоментил на каждое туду  чтобы не сливалось все подряд!!!

# for r in range(35, 50, 5):
#     circle(center_position=Point(100, 100), radius=r, color=sd.COLOR_DARK_RED)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет


def bubble(x, y, step, colors, radius):
    for _ in range(step):
        radius += step
        circle(center_position=Point(x, y), radius=radius, color=colors)

# bubble(100, 100, 52, sd.COLOR_GREEN, 25)

# Нарисовать 10 пузырьков в ряд

# for x in range(100,1100,100):
#     circle(center_position=Point(x, 100), radius=50, color=sd.COLOR_DARK_RED)

    # Нарисовать три ряда по 10 пузырьков


#for y in range(100, 400, 100):
#    for x in range(100, 1100, 100):
#        circle(center_position=Point(x, y), radius=50, color=sd.COLOR_DARK_RED)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for i in range(100):
    x = random.randint(100, 1000)
    y = random.randint(100, 600)
    circle(center_position=Point(x, y), radius=40, color=sd.random_color())

sd.pause()
