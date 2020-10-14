# -*- coding: utf-8 -*-

# Зачем нужны виртуальные окружения.
#
# Когда программист работает над несколькими проектами, то практически всегда бывает конфликт
# версий пакетов. Напрмер, в 2017 году сделал сайт на django 1.9, отдал заказчику - все норм.
# В 2018 - делаешь другой проект на django 2.0, установив его в системный пайтон.
# Возвращается первый заказчик и просит переделать старый проект.
# Можно конечно каждый раз переустанавливать django...
# А если таких пакетов - 25? а таких проектов - 5?
#
# Сделали возможность сделать "комнату" для пакетов: место где они все установлены нужных версий.
# Нужно работать над одним проектом - заходишь в первую комнату, над вторым - в другую, и т.п.
#
# Но для начала - где хранятся пакеты?
# Системные поставляются вместе с пайтоном и лежат в директории инсталляции C:\Python36-32\Lib
# Сторонние, устанавливаемые через pip - в директории C:\Python36-32\Lib\site-packages
#
# Python ищет модули для импорта по переменной окружения PATH (в первом приближении,
# на самом деле в пайтоне встроен настраиваемый механизм поиска модулей).
# Поэтому изменив эту переменную, можно сделать так, что бы интерпретатор работал с определенным набором
# пакетов. Делают так: создают папку, в неё складывают нужные пакеты и меняют PATH, добавляя эту папку
# в начало списка.
#
# Это все делает встроенный модуль venv: python -m venv probe_env
# Он создает папку, в который помещает необходимые скрипты и пакеты.
#
# Активировать окружение - войти в комнату - выполнить скрипт probe_env\Scripts\activate.bat
# И уже в этом окружениии ставить пакеты: pip install <имя пакета>
# Для выхода - deactivate в консоли.
#
# Посмотреть какие пакеты установлены: pip freeze
# Ага, попали все пакеты из системного пайтона :(
#
############ Поэтому правило всех разработчиков - не загрязнять системный пайтон! #############
############ Все пакеты ставить в окружение проекта! #############
#
# Надо почистить системный пайтон - переустановим и заодно обновимся.
#
# Смотрим что в системном?
#   pip freeze
# пусто - ок.
# Делаем виртуальное окружение,
#   python -m venv probe_env
# активируем,
#   probe_env\Scripts\activate.bat
# добавляем пакеты,
#   pip install simple_draw
# смотрим что установилось.
#   pip freeze
# Видим pygame и simple_draw. Ок.
#
# В соседнем окне смотрим что установлено в системном
#   pip freeze
# пусто. Ок.
# То есть мы можем организовать сколько угодно виртуальных окружений для работы с разными проектами
#
# Где хранить окружения? Обычно делают в самом проекте: папки env, venv, .env, .venv
# Мы сделаем так же.
#
# А как перевести пайчарм на виртуальлные окружения? Добавить интрепретатор в настройках.
#
# Сам пайчарм может создавать за нас виртуальные окружения.
# Но под капотом он выполняет все тот же python -m venv <>
#
# Отличия для linux(debian) и MacOS X
# Системные поставляются вместе с пайтоном и лежат в системной директории - /usr/lib/python3.x
# Сторонние, устанавливаемые через pip - /usr/local/lib/python3.x/site-packages
