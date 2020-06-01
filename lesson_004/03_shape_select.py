# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def geometry(point, angles=3, length=100, color=sd.COLOR_YELLOW):
    point_1 = point
    for angle in range(0, angles, 1):
        v = sd.get_vector(point, angle=angle * (360 // angles), length=length)
        point = v.end_point
        v.draw(color)
    sd.line(point_1, point, color=color)


geometry_text = {3: 'Треугольник', 4: 'Квадрат', 5: 'Пятиугольник', 6: 'Шестиугольник'}
print('Возможные фигуры:')
for key, value in geometry_text.items():
    print(f'      {key - 2} : {value}')
while True:
    cnt = input('Введите номер желаемой фигуры > ')
    cnt = int(cnt) + 2
    # TODO тут тоже сделай без else, как я писал во втором задании
    if cnt not in geometry_text:
        print('Не верный номер!')
        continue
    else:
        geometry(sd.Point(250, 250), int(cnt))
        break

# по примеру и заданию сделать надо по 4 фигурам


sd.pause()
