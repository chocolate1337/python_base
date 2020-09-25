# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
from collections import defaultdict
import pandas as pd
import numpy as np
from threading import Thread


class Volatility(Thread):

    def __init__(self, dir_in, mode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir_in = os.path.normpath(dir_in)
        self.prices = defaultdict(float)
        self.l_prices = []
        self.zero_volatility = []
        self.mode = mode

    def collect_prices(self):
        for root, dirs, filenames in os.walk(self.dir_in):
            for file in filenames:
                full_file_path = os.path.join(root, file)
                names = file[7:11]
                df = pd.read_csv(full_file_path, dtype={'PRICE': np.float32})
                new_date = df['PRICE'].describe(include='number')
                half_sum = (new_date.loc['max'] + new_date.loc['min']) / 2
                volatility = ((new_date.loc['max'] - new_date.loc['min']) / half_sum) * 100
                if volatility == 0:
                    self.zero_volatility.append(names)
                else:
                    self.prices[names] = volatility

    def run(self):
        self.collect_prices()
        self.l_prices = list(self.prices.items())
        self.l_prices.sort(key=lambda i: i[1])
        if self.mode == 'max':
            print('Максимальная волатильность:')
            print(self.l_prices[-3:])
        if self.mode == 'min':
            print('Минимальная волатильность:')
            print(self.l_prices[:3])
        if self.mode == 'zero':
            print('Нулевая волатильность:')
            print(self.zero_volatility)

path = os.path.join(os.path.dirname(__file__), 'trades')
volatility = [Volatility(dir_in=path,mode='max'),
              Volatility(dir_in=path,mode= 'min'),
              Volatility(dir_in=path,mode= 'zero')]

def run_in_threads(volatility):
    for vol in volatility:
        vol.start()
    for vol in volatility:
        vol.join()
run_in_threads(volatility)