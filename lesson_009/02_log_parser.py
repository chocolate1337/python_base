# -*- coding: utf-8 -*-
import time
import zipfile
from collections import defaultdict
import re


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

    def __init__(self, file_in, file_out):
        self.file_in = file_in
        self.file_out = file_out
        self.date_count = defaultdict(int)

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_in, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        # TODO В следующей строке лучще добавить отступ и
        #  устанавливать self.file_name в цикле.
        self.file_in = filename

    def sorting(self):
        print('Выберите режим сортировки 1 - по минутам')
        print('Выберите режим сортировки 2 - по часам')
        print('Выберите режим сортировки 3 - по месяцу')
        print('Выберите режим сортировки 4 - по году')
        mode = input()
        # TODO Здесь можно сделать проще, если использовать срезы.
        #  Для минут можно использовать строку 2018-05-14 19:44,
        #  для часов 2018-05-14 19. Использование регулярных выражений
        #  более ресурсозатратно, чем использование срезов строк.
        if mode == '1':
            self.date_patterns = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
        elif mode == '2':
            self.date_patterns = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}).+\]')
        elif mode == '3':
            self.date_patterns = re.compile('\[(\d{4}-\d{2}).+\]')
        elif mode == '4':
            self.date_patterns = re.compile('\[(\d{4}).+\]')
        else:
            print('Режим по умолчанию - 1')
            self.date_patterns = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')

    def collect(self):
        self.sorting()
        if self.file_in.endswith('.zip'):
            self.unzip()
        with open(self.file_in, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    catch = self.date_patterns.search(line)
                    if catch:
                        self.date = catch.group(1)
                        self.date_count[self.date] += 1

    def write(self):
        with open(self.file_out, 'w', encoding='utf8') as file:
            for date, cnt in self.date_count.items():
                line = f'[{date}] {cnt} \n'
                file.write(line)

# TODO Попробуйте изменить задание, используя шаблонны метод, как написано в первом задании.

file = DateTime(file_in='events.txt', file_out='out.txt')
file.collect()
file.write()
# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
