# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1 import room1 as central_h1_r1, room2 as central_h1_r2
from district.central_street.house2 import room1 as central_h2_r1, room2 as central_h2_r2
from district.soviet_street.house1 import room1 as soviet_h1_r1, room2 as soviet_h1_r2
from district.soviet_street.house2 import room1 as soviet_h2_r1, room2 as soviet_h2_r2

districts = [*central_h1_r1.folks,
             *central_h1_r2.folks,
             *central_h2_r1.folks,
             *central_h2_r2.folks,
             *soviet_h1_r1.folks,
             *soviet_h1_r2.folks,
             *soviet_h2_r1.folks,
             *soviet_h2_r2.folks]

print(f"На районе живут: {', '.join(districts)}")

# зачет!
