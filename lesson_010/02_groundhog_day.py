# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    def __str__(self):
        return 'IamGodError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


class SuicideError(Exception):
    def __str__(self):
        return 'SuicideError'


carma_level = 0
days = 0
errors = [IamGodError, DrunkError,
          CarCrashError, GluttonyError,
          DepressionError, SuicideError,
          ]


def one_day():
    carma = random.randint(1, 7)
    bad_day = random.randint(1, 13)
    rand = random.randint(0, 5)
    error = errors[rand]
    if bad_day == 13:
        try:
            raise Exception(error)
        except Exception:
            print(f'В этот день случилось ужасное - {error.__str__(self=error)} карма = 0')
            carma = 0
    return carma


while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
    carma_level += one_day()
    days += 1
    print(f'День номер - {days}, уровень кармы - {carma_level}')
print(f'За {days} - дня(ей,ень), герой достиг просветления!')
# https://goo.gl/JnsDqu
