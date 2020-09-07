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
# TODO создай классы своих ошибок, и их отлавливай
ENLIGHTENMENT_CARMA_LEVEL = 777
errors = ['IamGodError', 'DrunkError',
          'CarCrashError', 'GluttonyError',
          'DepressionError', 'SuicideError',
          ]
carma_level = 0
days = 0


def one_day():
    # TODO в try помещай код, в котором мождет быть ошибка, и можно ещё пару строк, если так удобнее, но не такие блоки.
    try:
        carma = random.randint(1, 7)
        bad_day = random.randint(1, 13)
        if bad_day == 13:
            rand = random.randint(0, 5)
            error = errors[rand]
            raise BaseException(error)
        return carma
    except BaseException: # TODO обычно если хотят отловить вообще все ошибки, то отлавливают Exception
        print(f'В этот день случилось ужасное - {error} карма = 0')
        # TODO чтобы в ф-ии не было 2 ретурна, можно тут сделать carma = 0 и в конце ф-ии вернуть carma
        return 0


while carma_level < ENLIGHTENMENT_CARMA_LEVEL:
    carma_level += one_day()
    days += 1
    print(f'День номер - {days}, уровень кармы - {carma_level}')
print(f'За {days} - дня(ей,ень), герой достиг просветления!')
# https://goo.gl/JnsDqu
