import simple_draw as sd

global number_flakes
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall

sd.resolution = [600, 600]
points = {}
N = 10

# TODO n - маленькую надо писать, это же не константа тут
def create_snowflake(N):
    for snow in range(1, N + 1, 1):
        # TODO желательно, чтобы снежинки шли сверху)
        points[snow] = sd.random_point()


def draw_snowflake(colors):
    for point in points.values():
        sd.snowflake(center=point, color=colors, length=30)


def move_snowflake():
    for point in points.values():
        point.y -= 5
        point.x -= sd.random_number(-5, 5)
        sd.snowflake(center=point, length=30)


def number_low_snowflake():
    for number, point in points.items():
        if point.y < 0:
            print(f'снежинка {number} упала')


def delete_snowflake():
    for number, point in points.items():
        # TODO надо сделать ф-ию, которая будет возвращать индексы снежинок,
        #  которые упали и в этой уже принимать его и удалять.
        if point.y < 0:
            sd.snowflake(center=point, color=sd.background_color, length=30)
            points[number] = sd.random_point()
