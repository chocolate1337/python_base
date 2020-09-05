# -*- coding: utf-8 -*-
import zipfile
from collections import defaultdict
from datetime import datetime


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class DateTime:
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

    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out
        self.date_count = defaultdict(int)
        self.date = ''

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_in, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            self.file_in = filename

    def collect(self):

        if self.file_in.endswith('.zip'):
            self.unzip()
        with open(self.file_in, 'r', encoding='utf8') as ff:
            for line in ff:
                if 'NOK' in line:
                    catch = datetime.strptime(line[1:self.modes[self.mode]], self.get_data[self.mode])
                    if catch:
                        self.date = catch
                        self.date_count[self.date] += 1

    def write(self):
        with open(self.file_out, 'w', encoding='utf8') as ff:
            for date, cnt in self.date_count.items():
                line = f'[{date}] {cnt} \n'
                ff.write(line)


class DateMode1(DateTime):
    mode = 1


class DateMode2(DateTime):
    mode = 2


class DateMode3(DateTime):
    mode = 3


class DateMode4(DateTime):
    mode = 4


file = DateMode1(file_in='events.txt', file_out='out.txt')
file.collect()
file.write()


# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году

# Зачёт!
