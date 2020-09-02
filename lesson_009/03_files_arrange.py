# -*- coding: utf-8 -*-

import os
import time
import shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class SortFiles:

    def __init__(self, dir_in, dir_out):
        self.dir_in = os.path.normpath(dir_in)
        self.dir_out = os.path.normpath(dir_out)
        self.secs = {}

    def read_path(self):
        for root, dirs, filenames in os.walk(self.dir_in):
            for file in filenames:
                full_file_path = os.path.join(root, file)
                self.secs[full_file_path] = time.gmtime(os.path.getmtime(full_file_path))
        self.create_sorted_files()

    def create_sorted_files(self):
        sorted_by_value = sorted(self.secs.items(), key=lambda kv: kv[1])
        for value in sorted_by_value:
            # TODO Вмето объединения частей пути через конкатенацию + "\\" +
            #  используйте os.path.join.
            new_dirs = (self.dir_out + "\\" + (time.strftime("%Y", value[1])) + "\\" + (time.strftime("%m", value[1])))
            new_dirs = os.path.normpath(new_dirs)
            if not os.path.exists(new_dirs):
                os.makedirs(new_dirs)
            shutil.copy(value[0], new_dirs)


# TODO Вмето объединения частей пути через конкатенацию + "\\" +
#  используйте os.path.join.
path_in = os.path.dirname(__file__) + '\\icons'
path_out = os.path.dirname(__file__) + '\\icons_by_year'
files = SortFiles(dir_in=path_in, dir_out=path_out)
files.read_path()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
