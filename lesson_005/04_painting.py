# -*- coding: utf-8 -*-
import simple_draw as sd

from forpaint import smile, rainbow, sun, branch, home

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

sd.resolution = [1200, 600]


def paint():
    flakes = [sun.Snowflake_Sun() for _ in range(10)]
    vectors = [sun.Snowflake_Sun().vector(angles=angles) for angles in range(0, 361, 30)]
    home.house()
    home.window_and_roof()
    branch.branch(sd.Point(900, 50), 90, 80)
    branch.branch(sd.Point(800, 50), 90, 30)
    branch.branch(sd.Point(1000, 50), 90, 30)
    while True:
        sd.start_drawing()
        smile.smile(550, 150, sd.COLOR_BLACK)
        sun.Snowflake_Sun().sun()
        for v in vectors:
            v.draw(sd.background_color, width=3)
            sun.Snowflake_Sun().sun()
            v.rotate(0.01)
            v.draw(width=3)
        # TODO все отлично, можно только этот
        #  цикл вынести в отдельную ф-ию снежной анимации.
        #  Чтобы уменьшить вложенность. Вообще ф-ии должны
        #  быть по 7-10 строк для читабельности.
        for flake in flakes:
            flake.draw_snow(color=sd.background_color)
            if flake.move():
                sd.rectangle(sd.Point(500, 110), sd.Point(600, 210), width=0)
                smile.smile1(550, 150, sd.COLOR_BLACK)
                flakes.insert(0, sun.Snowflake_Sun())
                flake.save_low_snow(color=sd.COLOR_WHITE)
                flakes.remove(flake)
            flake.draw_snow(color=sd.COLOR_WHITE)
        rainbow.rainbow()
        sd.finish_drawing()
        sd.sleep(0.05)
        if sd.user_want_exit():
            break


paint()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
