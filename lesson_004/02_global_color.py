# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE

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
# TODO ты можешь создать словарь более удобный,
#  который бы содержал все необходимые данные, типа
#  { 1: {'color_name': 'red', 'color_code': cd.COLOR_RED}, ...}
#  Так ты сразу сможешь получить и номер и имя цвета и код
color = [COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE]
color_text = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'CYAN', 'BLUE', 'PURPLE']
print('Возможные цвета:')
for i in enumerate(color):
    print(f'   {i[0] + 1}:{color_text[i[0]]}')
while True:
    cnt = input('Введите желаемый цвет > ')
    cnt = int(cnt)
    if (cnt > 7): # TODO тут скобки не нужны
        print('Не верный цвет')
    else:
        break

# TODO по кодингстайлу ф-ии выносятся вверх файла под импорты, а основной код - вниз.
#  Что у тебя за желтые точки в отрисовки фигуры?
def geometry(point, angle, length, *args):
    point_1 = point
    for count in args[0]:
        v = sd.get_vector(point, angle + count, length=length)
        point = v.end_point
        v.draw(color[cnt - 1], 4)
    sd.line(point_1, point)


geometry(sd.get_point(400, 100), 30, 100, [0, 90, 180, 270])
geometry(sd.get_point(150, 300), 30, 100, [0, 72, 144, 216, 288])
geometry(sd.get_point(400, 300), 30, 100, [0, 60, 120, 180, 240, 300])
geometry(sd.get_point(100, 100), 30, 100, [0, 120, 240])
#
sd.pause()
