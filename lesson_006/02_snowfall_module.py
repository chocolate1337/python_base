# -*- coding: utf-8 -*-
import simple_draw as sd
import snowfall as snow

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  TODO подсветил, какие ф-ии надо реализовать
#   создать_снежинки(N) - создает N снежинок
#   нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#   сдвинуть_снежинки() - сдвигает снежинки на один шаг
#   номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#   удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
N = 5
flakes = {}

for k in range(1, N):
    flakes[k] = snow.Snowflake()

while True:
    sd.start_drawing()
    for keys, flake in flakes.items():
        flake.draw_snow(color=sd.background_color)

        if flake.move():
            print(f'Снежинка под номером {keys} упала')
            # TODO зачем использовать магический метод __delitem__, если можно достать элемент с помощью []
            flakes.__delitem__(keys)
            flakes[keys] = snow.Snowflake()
        flake.draw_snow(color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit(sleep_time=0.1):
        break

sd.pause()
