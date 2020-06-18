import random




_bull_cows = {'Быков': 0, 'Коров': 0}

a_rand_number = []


def random_number():
    n = random.randint(1000, 9999)
    n = str(n)
    a_rand_number.extend(n)
    if len(a_rand_number) != len(set(a_rand_number)):
        a_rand_number.clear()
        random_number()
    else:
        return a_rand_number, print('Компьютер загадал число! Начинаем игру!', '\n')


global my_number
check = []

def valid_number(my_number):
    global check
    check.clear()
    check.extend(my_number)
    if len(check) == len(set(check)) and check[0] != 0 and len(check) == 4:
        check.clear()
        return True


def check_number(my_number):
    global cntBulls, cntCows
    cntBulls = 0
    cntCows = 0
    check.clear()
    check.extend(my_number)
    cntBulls = 0
    cntCows = 0
    for i in range(4):
        if check[i] == a_rand_number[i]:
            cntBulls += 1
        elif check[i] in a_rand_number:
            cntCows += 1
    _bull_cows['Быков'] = cntBulls
    _bull_cows['Коров'] = cntCows
    return _bull_cows

def play_again():
    play = input('Сыграем еще раз? 1 = Да, 2 = Нет ''\n')
    if play =='1':
        return True,random_number()

