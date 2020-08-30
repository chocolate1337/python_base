# -*- coding: utf-8 -*-
import collections
import operator
import zipfile


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.chars = collections.defaultdict(int)
        self.count = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        # TODO В следующей строке лучще добавить отступ и
        #  устанавливать self.file_name в цикле.
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.chars[char] += 1
                        self.count += 1

    def sorting(self):
        # TODO Нужно объявить self.sort_char в методе __init__.
        self.sort_char = {}
        print('Выберите режим сортировки 1 - частота букв по убыванию')
        print('Выберите режим сортировки 2 - частота букв по возрастанию')
        print('Выберите режим сортировки 3 - алфавит по убыванию')
        print('Выберите режим сортировки 4 - алфавит по возрастанию')
        mode = input()
        # TODO Нужно уменьшить дублирование кода и количество проверок.
        #  Вызовы sorted отличаются только индексом в
        if mode == '1':
            self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(1), reverse=True)
        elif mode == '2':
            self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(1), reverse=False)
        elif mode == '3':
            self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(0), reverse=True)
        elif mode == '4':
            self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(0), reverse=False)
        else:
            print('Режим по умолчанию - 1')
            self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(1), reverse=True)

    def __str__(self):
        print('+-------------+--------------+')
        print('|    буква    |    частота   |')
        print('+-------------+--------------+')
        for value in self.sort_char:
            print(f'|      {value[0]}      |    {value[1]:6d}    |')
        print('+-------------+--------------+')
        print(f'|    итого    |    {self.count}   |')
        print('+-------------+--------------+')
        return ''

# TODO  Задание получилось хорошо. Давайте сделаем одну оптимизацию и выполним требование
#  условия задания по использованию шаблонного метода.
#  Вызовы sorted отличаются только индексом в всех классов сортировки отличаются
#  только двумя параметрами:
#  - индекс в operator.itemgetter 0 или 1
#  - порядок сортировки reverse True или False.
#  Можно сделать эти параметры переменными класса и использовать
#  их внутри функции сортировки, а саму функцию сортировки перенести в общий класс.
#  Тогда останется добавить классы наследники в которых будет меняться только
#  две переменные для реализации всех типов сортировки.

# TODO Пример с демонстрацией отличия переменных класса от переменных экземпляра:
#
#  class MainClass:
#     variable1 = 0  # Это переменная класса
#
#      def __init__():
#           variable2 = 1  #  Это переменная экземпляра.
#  В результате должно получиться что-то подобное:
# class MainClass:
#     variable1 = 1
#
#     def __init__()
#         ...
#
# class Aggregation1(MainClass):
#     variable1 = 2
#
# class Aggregation2(MainClass):
#     variable1 = 3

files = CharStat(file_name='voyna-i-mir.txt')
files.collect()
files.sorting()
print(files)

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
