# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
from collections import defaultdict
from datetime import datetime

mode = 1
get_data = {1: '%Y-%m-%d %H:%M',
            2: '%Y-%m-%d %H',
            3: '%Y-%m',
            4: '%Y'
            }
modes = {1: 17,
         2: 14,
         3: 8,
         4: 5

         }
file_in = 'events.txt'
date_count = defaultdict(int)


def gropued_events():
    with open(file_in, 'r', encoding='utf8') as ff:
        for line in ff:
            if 'NOK' in line:
                catch = datetime.strptime(line[1:modes[mode]], get_data[mode])
                if catch:
                    date = catch
                    date_count[date] += 1
                    yield date, date_count[date]


date = gropued_events()
for k, v in date:
    date_count[k] = v
for k, v in date_count.items():
    print(k, v)
