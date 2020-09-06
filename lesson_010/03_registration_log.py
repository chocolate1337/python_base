# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


number_line = 1
numbers = str([1234567890])


def parse(line):
    if line is not None:
        name, email, age = line.split(' ')
        age = int(age)
        if "@" not in email:
            raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')
        elif age < 10 or age > 99:
            raise ValueError('Поле возраст НЕ является числом от 10 до 99')
        for values in numbers:
            if values in name:
                raise NotNameError('Поле имени содержит НЕ только буквы')
        return line
    elif line is None:
        raise ValueError('НЕ присутсвуют все три поля')
    else:
        return line


with open('registrations.txt', 'r') as ff:
    for line in ff:
        try:
            line = line[:-1]
            write = parse(line=line)
        except NotEmailError:
            with open('registrations_bad.log', 'a') as f_bad:
                write = f"Поле номер {number_line} - емейл НЕ содержит @ и .(точку)\n"
                f_bad.write(write)
        except NotNameError:
            with open('registrations_bad.log', 'a') as f_bad:
                write = f"Поле номер {number_line} - содержит НЕ только буквы\n"
                f_bad.write(write)
        except ValueError:
            with open('registrations_bad.log', 'a') as f_bad:
                write = f"Поле номер {number_line} - Неверные данные(Не верный возраст или пустое поле)\n"
                f_bad.write(write)
        else:
            with open('registrations_good.log', 'a') as f_good:
                write += '\n'
                f_good.write(write)
        number_line += 1
