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


class BadDayError(Exception):
    pass


class IamGodError(BadDayError):
    pass


class DrunkError(BadDayError):
    pass


class CarCrashError(BadDayError):
    pass


class GluttonyError(BadDayError):
    pass


class DepressionError(BadDayError):
    pass


class SuicideError(BadDayError):
    pass


carma_level = 0
days = 0
errors = [IamGodError, DrunkError,
          CarCrashError, GluttonyError,
          DepressionError, SuicideError,
          ]


def one_day():
    carma = random.randint(1, 7)
    bad_day = random.randint(1, 13)

    if bad_day == 13:
        try:
            rand = random.randint(0, 5)
            error = errors[rand]
            if rand == 0:
                raise error('IamGodError карма = 0')
            elif rand == 1:
                raise error('DrunkError карма = 0')
            elif rand == 2:
                raise error('CarCrashError карма = 0')
            elif rand == 3:
                raise error('GluttonyError карма = 0')
            elif rand == 4:
                raise error('DepressionError карма = 0')
            elif rand == 5:
                raise error('SuicideError карма = 0')
        except BadDayError:
            carma = 0
    return carma


while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
    carma_level += one_day()
    days += 1
    print(f'День номер - {days}, уровень кармы - {carma_level}')
print(f'За {days} - дня(ей,ень), герой достиг просветления!')
# https://goo.gl/JnsDqu
