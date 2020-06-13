import simple_draw as sd
sd.resolution = 1200, 600


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

    def vector(self, angles):
        return sd.get_vector(sd.Point(500, 500), angle=angles, width=3)

    def sun(self):
        sd.circle(sd.Point(500, 500), 40, width=0)

    def move(self):
        if self.y > self.length:
            self.y -= self.delta_y
            if self.y <= self.length + 50:
                return True
            self.x += sd.random_number(-10, +10)
        return False




def snowflake(flakes):
    for flake in flakes:
        flake.draw_snow(color=sd.background_color)
        if flake.move():
            sd.rectangle(sd.Point(500, 110), sd.Point(600, 210), width=0)
            flakes.insert(0, Snowflake_Sun())
            flake.save_low_snow(color=sd.COLOR_WHITE)
            flakes.remove(flake)
        flake.draw_snow(color=sd.COLOR_WHITE)


def sun_anim(vectors):
    Snowflake_Sun().sun()
    for v in vectors:
        v.draw(sd.background_color, width=3)
        Snowflake_Sun().sun()
        v.rotate(0.01)
        v.draw(width=3)
