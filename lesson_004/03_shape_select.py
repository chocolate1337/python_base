# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def geometry(point, angles=3, length=100, color=sd.COLOR_YELLOW):
    point_1 = point
    for angle in range(0, angles-1, 1):
        v = sd.get_vector(point, angle=angle * (360 // angles), length=length)
        point = v.end_point
        v.draw(color)
    sd.line(point_1, point, color=color)


geometry_text = {1: 'Треугольник', 2: 'Квадрат', 3: 'Пятиугольник', 4: 'Шестиугольник'}
print('Возможные фигуры:')
for key, value in geometry_text.items():
    print(f'      {key} : {value}')
while True:
    cnt = input('Введите номер желаемой фигуры > ')
    cnt = int(cnt)
    if cnt in geometry_text:
        geometry(sd.Point(250, 250), int(cnt+2))
        break
    print('Не верный номер!')



sd.pause()

# зачет!
