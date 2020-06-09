import simple_draw as sd

sd.resolution = 1200, 600
import simple_draw as sd


class Snowflake_Sun:

    def __init__(self, x=None, y=None, length=None):
        self.x = sd.random_number(0, 250) if x is None else x
        self.y = sd.random_number(300, sd.resolution[1]) if y is None else y
        self.length = sd.random_number(10, 40) if length is None else length
        self.delta_y = sd.random_number(10, 30)

    def draw_snow(self, color):
        if self.y > self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)

    def save_low_snow(self, color):
        if self.y < self.length:
            sd.snowflake(center=sd.Point(self.x, self.y), length=self.length, color=color)

    def vector(self,angles):
        return sd.get_vector(sd.Point(500, 500), angle=angles,width=3)
    def sun(self):
        sd.circle(sd.Point(500, 500), 40, width=0)


    def move(self):
        if self.y > self.length:
            self.y -= self.delta_y
            if self.y <= self.length + 50:
                return True
            self.x += sd.random_number(-10, +10)
        return False




