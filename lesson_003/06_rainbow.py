# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
x = 50
y = 50
end_x = 350
end_y = 450
iterable = 5
for s in rainbow_colors:
   sd.line(sd.Point(x, y), sd.Point(end_x, end_y), s, 4)
   x += iterable
   end_x += iterable

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

r = 350
for s in rainbow_colors:
    sd.circle(sd.Point(300, 50), r, s, 20)
    r += 20

sd.pause()
