# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

# BRUCE_WILLIS = 42
#
# input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
# leeloo = int(input_data[4])
# result = BRUCE_WILLIS * leeloo
# print(f'- Leeloo Dallas! Multi-pass № {result}!')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print('Невозможно преобразовать к числу!!')
except IndexError:
    print('Выход за границы списка!!')
except:
    print('Что-то пошло не так..')

# зачет!
