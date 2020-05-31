# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

sd.resolution = 1200, 600

root_point = sd.get_point(500, 30)


#
# def branch(point,angle,length,delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point,angle=angle,length=length)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point,angle=angle,length=length)
#     v2.draw()
#     next_point1 = v2.end_point
#     next_point = v1.end_point
#     next_angle = angle + delta
#     next_angle1 = angle - delta
#     next_length = length * .75
#     branch(next_point, next_angle, next_length, 30)
#     branch(next_point1, next_angle1, next_length, 30)
#
# branch(point=root_point,angle=90,length=100,delta=30)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции

def branch(point, angle, length):
    if length < 5:
        return
    delta_random = sd.random_number(-14, 14)
    vector = sd.Vector(point, angle, length)
    vector.draw()
    coif_length = sd.random_number(-12, 12)
    coif_length = 75 + coif_length
    next_length = length * float(coif_length/100)
    branch(vector.end_point, angle-30 -delta_random, next_length)
    branch(vector.end_point, angle+30 + delta_random, next_length)


branch(root_point, 90, 100)

sd.pause()
