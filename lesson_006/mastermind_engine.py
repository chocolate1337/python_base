import random

_bull_cows = {'Быков': 0, 'Коров': 0}

a_rand_number = []


def random_number():
    n = random.randint(1000, 9999)
    n = str(n)
    a_rand_number.extend(n)
    while len(a_rand_number) != len(set(a_rand_number)):
        a_rand_number.clear()
        n = random.randint(1000, 9999)
        n = str(n)
        a_rand_number.extend(n)
    return a_rand_number



def valid_number(my_number):
    if len(my_number) == len(set(my_number)) and my_number[0] != 0 and len(my_number) == 4:
        return True


def check_number(my_number):
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
    return _bull_cows



