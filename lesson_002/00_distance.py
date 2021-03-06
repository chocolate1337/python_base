#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
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



distances = {'London': {'Moscow': distance_xy(london, moscow), 'Paris': distance_xy(london, paris)},
             'Moscow': {'London': distance_xy(moscow, london), 'Paris': distance_xy(moscow, paris)},
             'Paris':  {'London': distance_xy(paris, london), 'Moscow': distance_xy(paris, moscow)}}

pprint.pprint(distances)

# лучше конечно было по одному добавлять
# зачет!
