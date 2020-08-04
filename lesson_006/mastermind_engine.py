import random

# TODO не уверен, что нужна эта переменная глобально, ты в check_number
#  можешь просто возвращать словарь, я там указал, как
_bull_cows = {'Быков': 0, 'Коров': 0}

a_rand_number = []


def random_number():
    # TODO лучше внутри цикла делать проверку и если условие выполняется, то break,
    #  а не 2 раза генерировать число в разных местах кода.
    n = random.randint(1000, 9999)
    n = str(n)
    a_rand_number.extend(n)
    while len(a_rand_number) != len(set(a_rand_number)):
        a_rand_number.clear()
        n = random.randint(1000, 9999)
        n = str(n)
        a_rand_number.extend(n)
    print(a_rand_number)
    return a_rand_number


def valid_number(my_number):
    if len(my_number) == len(set(my_number)) and my_number[0] != 0 and len(my_number) == 4:
        return True
    # TODO тут следует false возвращать, т.к. сейчас у тебя ф-ия возвращает true/none


def check_number(my_number):
    # TODO а что за нейминг переменных? Надо через _
    global cntBulls, cntCows
    cntBulls = 0
    cntCows = 0
    for idx in range(4):
        if my_number[idx] == a_rand_number[idx]:
            cntBulls += 1
        elif my_number[idx] in a_rand_number:
            cntCows += 1
    _bull_cows['Быков'] = cntBulls
    _bull_cows['Коров'] = cntCows
    # TODO просто вернуть {'Быков': cntBulls, 'Коров': cntCows}
    return _bull_cows
