# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

class ParseError(Exception):
    pass


class NotNameError(ParseError):
    pass


class NotEmailError(ParseError):
    pass


class AgeError(ParseError):
    pass


class InputError(ParseError):
    pass

def logs(file):
    def log_errors(func):
        def error(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, ParseError, ZeroDivisionError) as exc:
                with open(str(file), 'a') as f_bad:
                    write = f'Name: {func.__name__}, Args:{str(*args)} Error:{type(exc)} Invalid format: {exc} \n'
                    f_bad.write(write)
        return error
    return log_errors


# Проверить работу на следующих функциях
@logs('function_errorss.log')
def perky(param):
    return param / 0


@logs('function_errorss.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise NotNameError("it's not a name")
    if '@' not in email or '.' not in email:
        raise NotEmailError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise AgeError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

perky(42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

# зачет!
