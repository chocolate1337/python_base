#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

print(my_favorite_movies[0:10], # TODO если начинается с нуля, то 0 можно не указывать
      my_favorite_movies[-16:], # TODO тут лишний пробел
      my_favorite_movies[12:25],
      my_favorite_movies[-22:-17])
