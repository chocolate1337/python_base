import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные




# def snowflake_fall(fall_y,x):
#      y=600
#      while True:
#          sd.start_drawing()
#          point = sd.Point(x,y)
#          sd.snowflake(point, length=20,color=sd.background_color)
#          y-=fall_y
#          point1 = sd.Point(x,y)
#          sd.snowflake(point1,length=20)
#
#          if y<10:
#             sd.sleep(0.1)
#             sd.snowflake(point1, length=20)
#             y=600
#             x= sd.random_number(0,600)
#
#          sd.sleep(0.1)
#          sd.finish_drawing()
#
# snowflake_fall(30,300)
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

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
                return True
            self.x += sd.random_number(-10, +10)
        return False


def snowfall(N):
    flakes = [Snowflake() for _ in range(N)]
    while True:
        sd.start_drawing()
        for flake in flakes:
            flake.draw_snow(color=sd.background_color)
            if flake.move():
                flakes.append(Snowflake())
            flake.save_low_snow(color=sd.COLOR_WHITE)
            flake.draw_snow(color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(0.1)
        # TODO лучше просто упавшие снежинки поднимай наверх, внизу последний раз отрисовать как сугроб и поднять наверх
        if len(flakes) > 100:
            sd.clear_screen()
            flakes.clear()
            flakes = [Snowflake() for _ in range(N)]
        if sd.user_want_exit(sleep_time=0.1):
            break


snowfall(25)
