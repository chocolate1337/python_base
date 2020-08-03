# -*- coding: utf-8 -*-
import simple_draw as sd
from snowfall import create_snowflake,draw_snowflake,move_snowflake,number_low_snowflake,delete_snowflake

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

create_snowflake(10)
while True:
    sd.start_drawing()
    draw_snowflake(sd.background_color)
    move_snowflake()
    draw_snowflake(sd.COLOR_WHITE)
    sd.finish_drawing()
    number_low_snowflake()
    delete_snowflake()
    sd.sleep(0.01)
    if sd.user_want_exit(sleep_time=0.1):
        break

sd.pause()
