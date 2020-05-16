#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def distance_xy(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


moscow = sites['Moscow']

london = sites['London']

paris = sites['Paris']
# TODO нет, тут нужен словарь словарей, вот такой должен быть результат
# {'London': {'Moscow': 145.60219778561037, 'Paris': 42.42640687119285},
#  'Moscow': {'London': 145.60219778561037, 'Paris': 130.38404810405297},
#  'Paris': {'London': 42.42640687119285, 'Moscow': 130.38404810405297}}
distances = {
    'Moscow_to_Paris': (distance_xy(moscow, paris)),
    'Moscow_to_London': (distance_xy(moscow, london)),
    'Paris_to_Moscow': (distance_xy(paris, moscow)),
    'Paris_to_London': (distance_xy(paris, london)),
    'London_to_Paris': (distance_xy(london, paris)),
    'London_to_Moscow': (distance_xy(london, moscow)),
}

for key, value in distances.items():
    print(key, ' : ', value, sep='')
