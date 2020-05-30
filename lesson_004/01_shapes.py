# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import vector


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# ЗАКОМЕНТИЛ ФУНКЦИИ


# def triangle(point, angle=0, length=100):
#     point_1=point
#     for count in range(0, 241, 120):
#         v = sd.get_vector(point, angle + count, length=length)
#         point = v.end_point
#         v.draw()
#     sd.line(point_1,point)
#
# triangle(sd.Point(100, 100), 30, 100)
#
#
# def square(point, angle=0, length=100):
#     point_1 = point
#     for count in range(0, 360, 90):
#         v = sd.get_vector(point, angle + count, length=length)
#         point = v.end_point
#         v.draw()
#     sd.line(point_1, point)
#
#
# square(sd.Point(400, 100), 30, 100)
#
#
# def pentax(point, angle=0, length=100):
#     point_1 = point
#     for count in range(0, 289, 72):
#         v = sd.get_vector(point, angle + count, length=length)
#         point = v.end_point
#         v.draw()
#     sd.line(point_1,point)
#
# pentax(sd.Point(150, 350), 30, 100)
#
#
# def pentax_1(point, angle=0, length=100):
#     point_1 = point
#     for count in range(0, 360, 60):
#         v = sd.get_vector(point, angle + count, length=length)
#         point = v.end_point
#         v.draw()
#     sd.line(point_1,point)
#
#
# pentax_1(sd.Point(450, 350), 30, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

# TODO сделай, чтобы у тебя фигура принимала кол-во углов и точку рисования и длину,
#  а все остальные параметры высчитывала сама

def geometry(point, length, angle_cnt=3, colors=sd.COLOR_YELLOW):
    points = {
        angle_cnt == 3: point,
        # TODO зачем тут это? если у тебя ф-я принимает точку рисования уже.
        angle_cnt == 4: sd.Point(500, 100),
        angle_cnt == 5: sd.Point(200, 300),
        angle_cnt == 6: sd.Point(500, 300),
    }
    point = points[True]
    if colors not in sd.COLOR_YELLOW:
        # TODO зачем тут это? Сделай простую ф-ию, которая по входным параметрам рисует фигуру, без всех этих проверок
        colors.__add__(colors)
    angle = 0
    for count in range(0, angle_cnt, 1):
        v = sd.Vector(start_point=point, length=length, direction=sd._to_radians(angle))
        if count == angle_cnt - 1:
            point1 = sd.Point(point.x + length + 1, point.y + 1)
            sd.line(point, point1)
            break
        v.rotate(sd._to_radians(360 / angle_cnt + count * (360 / angle_cnt)))
        point = v.end_point
        v.draw(color=colors)
    angle_cnt += 1
    if angle_cnt > 6:
        return
    geometry(point, angle_cnt=angle_cnt, length=length)


geometry(angle_cnt=3, point=sd.Point(200, 100), length=100)

sd.pause()
