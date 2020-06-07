import random




cntBulls=0
cntCows =0


_bull_cows = {'Быков': cntBulls,'Коров': cntCows}



a_rand_number = []
def random_number():
  n = random.randint(1000,9999)
  n = str(n)
  a_rand_number.extend(n)
  if len(a_rand_number) != len(set(a_rand_number)):
    a_rand_number.clear()
    random_number()
  else:
    return a_rand_number, print('Компьютер загадал число! Начинаем игру!', '\n')

global N
check = []


def check_input(N):
  global check
  check.clear()
  check.extend(N)
  if len(check) == len(set(check)) and check[0]!=0 and len(check)==4:
    check.clear()
    return True



def check_number(N):
  global cntBulls,cntCows
  check.clear()
  check.extend(N)
  cntBulls = 0
  cntCows = 0
  for i in range(4):
    if check[i] == a_rand_number[i]:
      cntBulls+=1
    if check[i] in a_rand_number and check[i]!=a_rand_number[i]:
      cntCows+=1
  _bull_cows['Быков']=cntBulls
  _bull_cows['Коров'] = cntCows
  return _bull_cows

def game_over():
  if cntBulls==4:
    return True



