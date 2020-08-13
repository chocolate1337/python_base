# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, x=None, y=None, length=None):
        self.x = sd.random_number(0, sd.resolution[0]) if x is None else x
        self.y = sd.random_number(300, sd.resolution[1]) if y is None else y
        self.length = sd.random_number(10, 40) if length is None else length
        self.delta_y = sd.random_number(10, 30)

    def draw_snow(self, color):
        if self.y > self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)

    def save_low_snow(self, color):
        if self.y < self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)

    def move(self):
        if self.y > self.length:
            self.y -= self.delta_y
            if self.y <= self.length:
                return False
            self.x += sd.random_number(-10, +10)
        return True

def snowfall(n):
    flakes = [Snowflake() for _ in range(n)]
    while True:
        sd.start_drawing()
        for flake in flakes:
            flake.draw_snow(color=sd.background_color)
            if not flake.move():
                flakes.append(Snowflake())
                flake.save_low_snow(color=sd.COLOR_WHITE)
                flakes.remove(flake)
            flake.draw_snow(color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit(sleep_time=0.1):
            break


snowfall(25)

sd.pause()
