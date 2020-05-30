# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE


def geometry(point, length, angle_cnt=3, colors=sd.COLOR_YELLOW):
    points = {
        angle_cnt == 3: point,
        angle_cnt == 4: sd.Point(500, 100),
        angle_cnt == 5: sd.Point(200, 300),
        angle_cnt == 6: sd.Point(500, 300),
    }
    point = points[True]
    if colors not in sd.COLOR_YELLOW:
        colors.__add__(colors)
    angle = 0
    for count in range(0, angle_cnt, 1):
        v = sd.Vector(start_point=point, length=length, direction=sd._to_radians(angle))
        if count == angle_cnt - 1:
            point1 = sd.Point(point.x + length + 1, point.y + 1)
            sd.line(point, point1, color=colors)
            break
        v.rotate(sd._to_radians(360 / angle_cnt + count * (360 / angle_cnt)))
        point = v.end_point
        v.draw(color=colors)
    angle_cnt += 1
    if angle_cnt > 6:
        return
    geometry(point, angle_cnt=angle_cnt, length=length, colors=s)


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

# тут хорошо
color = {1: {'color_name': 'red', 'color_code': COLOR_RED},
         2: {'color_name': 'orange', 'color_code': COLOR_ORANGE},
         3: {'color_name': 'yellow', 'color_code': COLOR_YELLOW},
         4: {'color_name': 'green', 'color_code': COLOR_GREEN},
         5: {'color_name': 'cyan', 'color_code': COLOR_CYAN},
         6: {'color_name': 'blue', 'color_code': COLOR_BLUE},
         7: {'color_name': 'purple', 'color_code': COLOR_PURPLE},
         }
print('Возможные цвета:')
for number, key in color.items():
    print(f"{number} : {key['color_name']}")
while True:
    cnt = input('Введите желаемый цвет > ')
    try:
        # TODO ты можешь введенное число проверять на вхождение в color с помощью оператора in.
        #  Тогда не надо будет делать try/except
        if int(cnt) > 7:
            print('Не верный цвет')
        else:
            break
    except ValueError:
        print('Не верный цвет')
        continue

print(f"{color[int(cnt)].__getitem__('color_code')}")
s = color[int(cnt)].__getitem__('color_code')
geometry(sd.Point(200, 100), 100, colors=s)

# TODO по кодингстайлу ф-ии выносятся вверх файла под импорты, а основной код - вниз.
#  Что у тебя за желтые точки в отрисовки фигуры?

#
sd.pause()
