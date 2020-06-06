# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from lesson_005 import room_1 as r1,room_2 as r2

print(f"На районе живут {','.join(r1.folks)},{','.join(r2.folks)}")



