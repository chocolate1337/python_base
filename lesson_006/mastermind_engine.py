import random

a_rand_number = []


def random_number():
    while True:
        a_rand_number.clear()
        n = random.randint(1000, 9999)
        n = str(n)
        a_rand_number.extend(n)
        if len(a_rand_number) == len(set(a_rand_number)):
            break
    return a_rand_number


def valid_number(my_number):
    # TODO тут можно так сделать, т.к. у тебя ф-ия возвращала либо true, либо none.
    return len(my_number) == len(set(my_number)) and my_number[0] != 0 and len(my_number) == 4


def check_number(my_number):
    # TODO зачем эти глобальные переменные?
    global bulls, cows
    bulls = 0
    cows = 0
    for idx in range(4):
        if my_number[idx] == a_rand_number[idx]:
            bulls += 1
        elif my_number[idx] in a_rand_number:
            cows += 1
    return {'Быков': bulls, 'Коров': cows}
