# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def geometry(point, angle=30, length=100):
        point_1 = point
        for angles in range(0, n - 1, 1):
            v = sd.get_vector(point, angle=angles * (360 // n) + angle, length=length)
            point = v.end_point
            v.draw()
        sd.line(point_1, point)
    return geometry


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=1, length=50)


sd.pause()
