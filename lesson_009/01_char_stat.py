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

class ReadData:

    def __init__(self, file_name):
        self.file_name = file_name
        self.sort_char = {}
        self.chars = collections.defaultdict(int)
        self.count = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)

            self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()

    # TODO В следующей строке нужно исправить оформление, убравл лишние пробелы.
    def sorting(self, mode = 0, reverse = True):
        self.sort_char = sorted(self.chars.items(), key=operator.itemgetter(mode), reverse=reverse)

    def save(self):
        with open(self.file_name, 'wb') as ff:
            ff.write(self.file_name)

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


class CharStat(ReadData):
    # TODO Нет необходимости в создании класса CharStat.
    #  Создавать отдельные классы нужно для реализации разных типов сортировки.
    #  В основном классе объявляются переменные класса mode и reverse и используются
    #  в методе sorting вместо аргументов.
    #  Про шаблонный метод можно почитать по ссылкам выше в задании.
    #  В классах наследниках достаточно будет поменять эти переменные класса.
    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.chars[char] += 1
                        self.count += 1


files = CharStat(file_name='voyna-i-mir.txt')
files.collect()
files.sorting(mode=1, reverse=False) # mode = 0 По буквам, 1 - по частоте
print(files)

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
