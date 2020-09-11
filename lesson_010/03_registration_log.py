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
# TODO почему тут ValueError?
class ParseError(ValueError):
    pass


class NotNameError(ParseError):
    pass


class NotEmailError(ParseError):
    pass


class AgeError(ParseError):
    pass


class InputError(ParseError):
    pass


number_line = 1
numbers = str([1234567890])


class Parse:

    def __init__(self, line):
        self.line = line
        self.name_v, self.email_v, self.age_v = self.line.split(' ')
        self.parse()

    def parse(self):
        if self.line is not None:
            self.age()
            self.email()
            self.name()
            return self.line
        elif self.line is None:
            raise InputError('НЕ присутсвуют все три поля')
        else:
            return self.line

    def email(self):
        if "@" not in self.email_v:
            raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')

    def age(self):
        self.age_v = int(self.age_v)
        if self.age_v < 10 or self.age_v > 99:
            raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')

    def name(self):
        for values in numbers:
            if values in self.name_v:
                raise NotNameError('поле имени содержит НЕ только буквы')

    def __str__(self):
        return self.line


def write_log(write, number_line):
    with open('registrations_bad.log', 'a') as f_bad:
        line = f"Поле номер {number_line} -" + write + '\n'
        f_bad.write(line)


with open('registrations.txt', 'r') as ff:
    for line in ff:
        try:
            line = line[:-1]
            parse = Parse
            write = parse(line)
        except NotEmailError:
            write_log(write='поле емейл НЕ содержит @ и .(точку)', number_line=number_line)
        except NotNameError:
            write_log(write='поле имени содержит НЕ только буквы', number_line=number_line)
        except AgeError:
            write_log(write='поле возраст НЕ является числом от 10 до 99', number_line=number_line)
        except (InputError, ValueError):
            write_log(write='НЕ присутсвуют все три поля', number_line=number_line)

        else:
            with open('registrations_good.log', 'a') as f_good:
                f_good.write(str(write))
                f_good.write('\n')
        number_line += 1
