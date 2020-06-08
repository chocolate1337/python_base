import simple_draw as sd
from forpaint import smile, rainbow

sd.resolution = 1200, 600
import simple_draw as sd


class Snowflake_Sun:

    def __init__(self, x=None, y=None, length=None):
        # TODO эти параметры по умолчанию лучше задать сразу в параметрах ф-ии
        self.x = sd.random_number(0, 250) if x is None else x
        self.y = sd.random_number(300, sd.resolution[1]) if y is None else y
        self.length = sd.random_number(10, 40) if length is None else length
        self.delta_y = sd.random_number(10, 30)
        self.v = sd.get_vector(sd.Point(500, 500), sd.random_number(0, 360), 80, 10)
        self.v.draw(sd.background_color)
        self.v2 = sd.get_vector(self.v.start_point, self.v.angle, length=80, width=3)
        self.v2.draw(color=sd.COLOR_YELLOW)
        sd.circle(sd.Point(500, 500), 30, width=0)
        self.color = sd.COLOR_YELLOW

    def draw_snow(self, color):
        if self.y > self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)

    def save_low_snow(self, color):
        if self.y < self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)
    # TODO почему бы не сделать, чтобы лучи по кругу шли постоянно?
    def move(self):
        if self.y > self.length:
            self.y -= self.delta_y
            if self.y <= self.length + 50:
                return True
            self.x += sd.random_number(-10, +10)
        return False


def snowfall(N):
    flakes = [Snowflake_Sun() for _ in range(N)]
    while True:
        sd.circle(sd.Point(500, 500), 30, width=0)

        sd.start_drawing()
        # TODO анимацию надо реализовать в главном модуле,
        #  т.к. тут получается не логично, что в модуле солнце реализована анимация...
        #  Или создай модуль анимация и в нем реализуй анимацию.
        smile.smile(550, 150, sd.COLOR_BLACK)
        sd.circle(sd.Point(500, 500), 30, width=0)
        Snowflake_Sun.__call__()

        for flake in flakes:
            flake.draw_snow(color=sd.background_color)
            if flake.move():
                sd.rectangle(sd.Point(500, 110), sd.Point(600, 210), width=0)
                smile.smile1(550, 150, sd.COLOR_BLACK)
                flakes.insert(0, Snowflake_Sun())
                flake.save_low_snow(color=sd.COLOR_WHITE)
                flakes.remove(flake)
            flake.draw_snow(color=sd.COLOR_WHITE)
        print(len(flakes))  # просто для теста чтобы понять что список бесконечно не растет
        rainbow.rainbow()
        sd.finish_drawing()
        sd.sleep(0.01)
        if sd.user_want_exit(sleep_time=0.1):
            break
