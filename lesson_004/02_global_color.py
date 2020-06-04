# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE


def geometry(point, angles=3, length=100, color=COLOR_YELLOW):
    point_1 = point
    for angle in range(0, angles-1, 1):
        v = sd.get_vector(point, angle=angle * (360 // angles), length=length)
        point = v.end_point
        v.draw(color)
    sd.line(point_1, point, color=color)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# тут хорошо
color_dict = {1: {'color_name': 'red', 'color_code': COLOR_RED},
              2: {'color_name': 'orange', 'color_code': COLOR_ORANGE},
              3: {'color_name': 'yellow', 'color_code': COLOR_YELLOW},
              4: {'color_name': 'green', 'color_code': COLOR_GREEN},
              5: {'color_name': 'cyan', 'color_code': COLOR_CYAN},
              6: {'color_name': 'blue', 'color_code': COLOR_BLUE},
              7: {'color_name': 'purple', 'color_code': COLOR_PURPLE},
              }
print('Возможные цвета:')
for number, key in color_dict.items():
    print(f"{number} : {key['color_name']}")
while True:
    cnt = input('Введите желаемый цвет > ')
    if int(cnt) in color_dict:
      colors = color_dict[int(cnt)]['color_code']
      break
    print('не верный номер')


geometry(sd.Point(100, 100), 3, color=colors)
geometry(sd.Point(400, 100), 4, color=colors)
geometry(sd.Point(100, 300), 5, color=colors)
geometry(sd.Point(400, 300), 6, color=colors)

#
sd.pause()
