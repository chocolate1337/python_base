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
# тут хорошо
class ParseError(ValueError):
    pass


class NotNameError(ParseError):
    # TODO тут тоже лучше метод не переопределять, а передавать сообщение при райзинге.
    def __str__(self):
        return 'поле имени содержит НЕ только буквы'


class NotEmailError(ParseError):
    def __str__(self):
        return 'поле емейл НЕ содержит @ и .(точку)'


class AgeError(ParseError):
    def __str__(self):
        return 'поле возраст НЕ является числом от 10 до 99'


class InputError(ParseError):
    def __str__(self):
        return 'НЕ присутсвуют все три поля'


number_line = 1
numbers = str([1234567890])


def parse(line):
    if line is not None:
        name, email, age = line.split(' ')
        age = int(age)
        # TODO возможно лучше сделать каждую валидацию в отдельной ф-ии, чтобы при добавлении новых валидаций не надо было расширять эту ф-ию до бесконечности, тем более, что может потребоваться добавить более сложную проверку. Также это можно было бы оформить в класс, и в нем сделать ф-ию валидации, которая бы вызывала все ф-ии, для отдельных валидаций.
        if "@" not in email:
            raise NotEmailError
        elif age < 10 or age > 99:
            raise AgeError
        for values in numbers:
            if values in name:
                raise NotNameError
        return line
    elif line is None:
        raise InputError
    else:
        return line


def write_log(write, number_line):
    with open('registrations_bad.log', 'a') as f_bad:
        line = f"Поле номер {number_line} -" + write + '\n'
        f_bad.write(line)


with open('registrations.txt', 'r') as ff:
    for line in ff:
        try:
            line = line[:-1]
            write = parse(line=line)
        except NotEmailError:
            write_log(write=NotEmailError.__str__(NotEmailError), number_line=number_line)
        except NotNameError:
            write_log(write=NotNameError.__str__(NotNameError), number_line=number_line)
        except AgeError:
            write_log(write=AgeError.__str__(AgeError), number_line=number_line)
        except (InputError, ValueError):
            write_log(write=InputError.__str__(InputError), number_line=number_line)

        else:
            with open('registrations_good.log', 'a') as f_good:
                write += '\n'
                f_good.write(write)
        number_line += 1
