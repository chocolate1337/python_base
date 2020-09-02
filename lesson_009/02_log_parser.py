# -*- coding: utf-8 -*-
import time
import zipfile
from collections import defaultdict
import re
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

class GetData:

    def __init__(self, input_file, output_file):
        self.input = input_file
        self.output = output_file

    def parse(self):
        with open(self.input, 'r', encoding='utf-8') as file:
            yield from file

    def write(self, str):
        with open(self.output, 'a', encoding='utf-8') as file:
            file.write(str)

    def filter(self, str):
        if 'NOK' in str:
            return str

    def get_date(self, str):
        date = datetime.strptime(str[1:str.index('.')], '%Y-%m-%d %H:%M:%S')
        return date

    def start(self):
        pass


# TODO Не понятно, для чего функциональность класса была разделена на два.
#  Реализация отдельных классов нужна при реализации шаблонного метода,
#  когда в классах населедниках заменяются некоторые меотды или переменны.
class Parser(GetData):

    def __init__(self, input_file, output_file, mode=1):
        super().__init__(input_file, output_file)
        modes = {
            0: ('second', '%Y-%m-%d %H:%M:%S'),
            1: ('minute', '%Y-%m-%d %H:%M'),
            2: ('hour', '%Y-%m-%d %H'),
            3: ('day', '%Y-%m-%d'),
            4: ('month', '%Y-%m'),
            5: ('year', '%Y')
        }
        self.mode = mode
        self.limit = modes[mode][0]
        self.time_format = modes[mode][1]

    def start(self):
        data = self.parse()
        count = 1
        prev = None
        # TODO Если вместо цикла while использовать цикл for, то не нужно будет считывать строки файла
        #  с обработкой исключений.
        while True:
            try:
                item = next(data)
            except StopIteration:
                if self.get_date(prev):
                    # TODO Запись в файл можно сделать отдельным методом, чтобы не дублировать код.
                    self.write(self.get_date(prev).strftime(self.time_format) + ' NOK ' + str(count) + '\n')
                break
            if self.filter(item):
                if prev is None:
                    if self.get_date(item):
                        prev = item
                else:
                    if self.get_date(item):
                        if getattr(self.get_date(item), self.limit) == getattr(self.get_date(prev), self.limit):
                            count += 1
                            prev = item
                        else:
                            self.write(self.get_date(prev).strftime(self.time_format) + ' NOK ' + str(count) + '\n')
                            count = 1
                            prev = item


# запуск в режиме по умолчанию
parser = Parser('events.txt', 'out.txt', 1)
parser.start()
# режим (0 - секунды, 1 - минуты, 2 - часы, 3 - дни, 4 - месяцы, 5 - годы)

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
