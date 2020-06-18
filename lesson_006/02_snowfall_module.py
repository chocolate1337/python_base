# -*- coding: utf-8 -*-
import simple_draw as sd
from snowfall import color_flake, move, point_xy, points

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

number_flakes = 5
point_xy(number_flakes)
while True:
    sd.start_drawing()
    color_flake(points, sd.background_color)
    move(points, number_flakes)
    color_flake(points, sd.COLOR_WHITE)
    # TODO тут надо вызывать ф-ию, которая вернет список индексов упавших снежинок.
    #  И потом его передать в ф-ию, которая удалит из списка снежинок эти снежинки.
    #  Ну и потом в ф-ию создания новых снежинок передаешь кол-во упавших снежинок и создаешь новые снежинки на место упавших.
    sd.finish_drawing()
    sd.sleep(0.01)
    if sd.user_want_exit(sleep_time=0.1):
        break

sd.pause()
