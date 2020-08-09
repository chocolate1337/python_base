import simple_draw as sd

# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall

sd.resolution = [600, 600]
points = {}

def create_snowflake(n):
    for snow in range(1, n + 1, 1):
        points[snow] = sd.Point(x=sd.random_number(0, 600), y=sd.random_number(500, 600))


def draw_snowflake(colors):
    for point in points.values():
        sd.snowflake(center=point, color=colors, length=30)


def move_snowflake():
    for point in points.values():
        point.y -= 25
        point.x -= sd.random_number(-5, 5)
        sd.snowflake(center=point, length=30)


def number_low_snowflake():
    numbers_fallen = []
    for number, point in points.items():
        if point.y < 10:
            numbers_fallen.append(number)
    return numbers_fallen


def delete_snowflake(numbers_fallen):
    print(f'Снежинки под номерами: {numbers_fallen} упали')
    for number in numbers_fallen:
        points[number] = sd.Point(x=sd.random_number(0, 600), y=sd.random_number(500, 600))
