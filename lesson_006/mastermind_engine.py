import random




cntBulls=0
cntCows =0


_bull_cows = {'Быков': cntBulls,'Коров': cntCows}



a = []
def random_number():
  n = random.randint(1000,9999)
  n = str(n)
  a.extend(n)
  if len(a) != len(set(a)):
    a.clear()
    random_number()
  return a

random_number()
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
    if check[i] == a[i]:
      cntBulls+=1
    if check[i] in a and check[i]!=a[i]:
      cntCows+=1
  _bull_cows['Быков']=cntBulls
  _bull_cows['Коров'] = cntCows
  return _bull_cows

def game_over():
  if cntBulls==4:
    return True



