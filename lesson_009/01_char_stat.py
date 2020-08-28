# -*- coding: utf-8 -*-
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

file_name = 'python_snippets\\voyna-i-mir.txt'

class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.chars = {}
        self.count = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        # TODO Можно не делать два прохода по одному и тому же файлу.
        #  Вместо этого нужно проверять, используя оператор in, есть ли
        #  уже в словаре ключ для добавляемого символа. Если ключ есть,
        #  то нужо увеличить значение, если ключа нет, то добавить в
        #  словарь запись с значением 1.
        #  Можно сделать более оптимальное решение, используя специально
        #  модифицированный словарь defaultdict или Counter из библиотеки
        #  collections. Нужно будет в методе __init__ заменить {} на
        #  collections.defaultdict(int), убрать оба метода (_collect_for_line
        #  и _count_for_line) а в цикле по строкам файла увеличивать значения
        #  в словаре self.chars[char] += 1.
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._count_for_line(line=line[:-1])


    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                self.chars[char] = 0

    def _count_for_line(self, line):
        for char in line:
            if char.isalpha():
                self.chars[char] += 1
                self.count += 1

    def prepare(self):
        # TODO Оптимальнее применить функцию sorted(self.chars.items()) для получения
        #  универсального способа сортировки. Аргумент reverse функции sorted влияет на
        #  порядок сортировки, а аргумент key нужно использовать вместе с функцией
        #  operator.itemgetter. Это позволит выбирать сортировать по ключам или по
        #  значениям словаря.
        self.list_chars = {}
        self.list_chars = list(self.chars.items())
        self.list_chars.sort(key=lambda i: i[1], reverse=True)

    def __str__(self):
        print('+-------------+--------------+')
        print('|    буква    |    частота   |')
        print('+-------------+--------------+')
        for value in self.list_chars:
            print(f'|      {value[0]}      |    {value[1]:6d}    |')
        print('+-------------+--------------+')
        print(f'|    итого    |    {self.count}   |')
        print('+-------------+--------------+')
        return ''

files = CharStat(file_name='voyna-i-mir.txt')
files.collect()
files.prepare()
print(files)


# TODO Обращайте внимание на предупреждения среды разработки о
#  проблемах в коде или нарушении стандарта PEP 8.
#  Попробуйте найти зеленую галочку справа над полосой прокрутки.
#  Если вместо нее, квадрат красного, желтого или серого цвета,
#  значит в файле есть недостатки оформления или ошибки.
#  Места с ошибками помечены цветными отметками на полосе прокрутки.

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
