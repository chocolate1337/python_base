# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import re

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import datetime
import calendar
import cv2
import numpy as np
import os.path as path
import sys
import fire
import os
from db import DatabaseUpdater

BASE_PATH = path.dirname(__file__)
BASE_PATH = path.normpath(BASE_PATH)

class WeatherMaker:
    """
    Weather parser for pogoda.mail.ru
    """

    def __init__(self):
        self.data = {}

    def get_data(self, period_from: str, period_to: str = None) -> dict:
        """
        Get data from site

        Args:
            period_from (str): start of period. Format: YYYY-MM-DD
            period_to (str, optional):  end of period. Format: YYYY-MM-DD. Default None

        Returns:
            dict: {date: datetime.date, day_temperature: str, night_temperature: str, etc.}
        """

        period_from = datetime.datetime.strptime(period_from, '%Y-%m-%d').date()

        if period_to:
            period_to = datetime.datetime.strptime(period_to, '%Y-%m-%d').date()
        else:
            period_to = period_from

        period_from_year, period_from_month, period_from_day = period_from.year, period_from.month, period_from.day
        period_to_year, period_to_month, period_to_day = period_to.year, period_to.month, period_to.day

        month_list = list(map(str.lower, calendar.month_name[period_from_month:period_to_month + 1]))

        for month in month_list:
            base_url = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'
            period_from_url = urljoin(base_url, f'{month}-{period_from_year}')
            response = requests.get(period_from_url).text
            month_soup_data = BeautifulSoup(response, features='html.parser')

            self.parse_weather(month_soup_data)

        # date filter
        period_weather = {k: v for k, v in self.data.items() if (k >= period_from) and (k <= period_to)}
        return period_weather

    def parse_weather(self, month_soup_data):
        # div-element with weather
        for day_div in month_soup_data.find_all('div', class_=re.compile(r'day day_calendar(?!\sday_title)')):

            # early stoping
            if day_div.find('div', class_='day__alternative'):
                continue

            # parse date
            text_date = re.search(r'(\d{1,2}\s[а-яА-Я]+\s\d{4})', day_div.find('div', class_='day__date').text)[0]
            year_num = int(re.search(r'\d{4}$', text_date)[0])
            text_month = re.search(r'[а-яА-Я]+', text_date)[0].lower()
            month_num = ['', 'января', 'февраля', 'марта', 'апреля', 'мая',
                         'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'].index(text_month)
            day_num = int(re.search(r'^\d{1,2}', text_date)[0])
            date = datetime.date(year_num, month_num, day_num)

            # parse weather
            day_info = self.data[date] = {}
            day_info['day_temperature'] = re.search(r'[+\-]\d{1,2}',
                                                    day_div.find('div', class_='day__temperature').text)[0]
            day_info['night_temperature'] = day_div.find('span', class_='day__temperature__night').text
            day_info['day_description'] = day_div.find_next('div', {'class': 'day__description'}).find('span').text
            day_info['pressure'] = day_div.find('span', title=re.compile('Давление')).text.strip()
            day_info['humidity'] = day_div.find('span', title=re.compile('Влажность')).text.strip()
            day_info['wind'] = day_div.find('span', title=re.compile('Ветер')).text.strip()


class ImageMaker:
    COLOR_SCHEMES = dict(
        white=np.array([255, 255, 255]),
        yellow=np.array([0, 255, 255]),
        blue=np.array([255, 50, 50]),
        whiteblue=np.array([255, 178, 102]),
        grey=np.array([192, 192, 192])
    )

    ICON_PATH = path.join(BASE_PATH, 'python_snippets', 'external_data', 'weather_img')
    ICONS = dict(
        cloud=path.join(ICON_PATH, 'cloud.jpg'),
        rain=path.join(ICON_PATH, 'rain.jpg'),
        snow=path.join(ICON_PATH, 'snow.jpg'),
        sun=path.join(ICON_PATH, 'sun.jpg')
    )

    def __init__(self):
        self.input_image = cv2.imread(path.join(BASE_PATH, 'python_snippets', 'external_data', 'probe.jpg'))
        self.output_image = self.input_image.copy()

    def make_gradient(self, color: str) -> None:
        """Make color gradiend."""

        blue, green, red = self.COLOR_SCHEMES[color]
        height, width, deep = self.input_image.shape

        column_color = np.hstack((
            np.linspace(blue, 255, height, dtype='uint8').reshape(height, 1),
            np.linspace(green, 255, height, dtype='uint8').reshape(height, 1),
            np.linspace(red, 255, height, dtype='uint8').reshape(height, 1),
        ))

        gradient = np.array(list(map(lambda x: np.array([x] * width), column_color)))
        self.output_image = gradient

    def put_text(self, text: str, font_scale: float = 0.8, color: tuple = (0, 0, 0),
                 thickness: int = 1, position: tuple = (100, 100)) -> None:
        """Put text to postcard.

        Args
            text (str): some text
            position(tuple): left-bottom text position
        """
        cv2.putText(img=self.output_image,
                    text=text,
                    org=position,
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=font_scale,
                    color=color,
                    thickness=thickness)

    def put_icon(self, icon_name: str, x: int = 412, y: int = 0, alpha: int = 0.2) -> None:
        """Put icon to postcard.

        Args
            icon_name (str): cloud/rain/snow/sun
            pos (tuple): icon position (y, x)
        """
        icon = cv2.imread(self.ICONS[icon_name])
        back = self.output_image
        icon_rows, icon_cols, icon_channels = icon.shape

        weighted_icon = cv2.addWeighted(back[y:icon_rows + y, x:icon_cols + x, :],
                                        alpha, icon, 1 - alpha, 0.2)

        back[y:icon_rows + y, x:icon_cols + x] = weighted_icon


class PostcardMaker:
    """Generate weather postcard."""

    ICON_SETTINGS = {
        # Солнечно - от желтого к белому
        # Дождь - от синего к белому
        # Снег - от голубого к белому
        # Облачно - от серого к белому
        'ясно': dict(icon='sun', color='yellow'),
        'облачно': dict(icon='cloud', color='grey'),
        'дождь': dict(icon='rain', color='blue'),
        'дождь/гроза': dict(icon='rain', color='blue'),
        'осадки': dict(icon='rain', color='blue'),
        'снег': dict(icon='snow', color='whiteblue')
    }

    def __init__(self):
        self.image_maker = ImageMaker()
        self.template = None
        self.date = None
        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.wind = None
        self.day_description = None
        self.icon_type = None
        self.gradient_color = None
        self.image = None

    def generate_postcard(self, weather):
        """Generate postcard"""
        self._parse_weather(weather)
        self._generate_template()
        self._generate_text()
        self.image = self.image_maker.output_image

    def show_image(self):
        if self.image is not None:
            cv2.imshow('weather', self.image)
            cv2.waitKey(0)

    def save_image(self, filename):
        if self.image is not None:
            cv2.imwrite(f'{filename}', self.image)

    def _generate_template(self):
        self.image_maker.make_gradient(self.gradient_color)
        self.image_maker.put_icon(self.icon_type)

    def _generate_text(self):
        # date
        date_string = datetime.date.strftime(self.date, "%d.%m.%Y")
        self.image_maker.put_text(text=date_string, font_scale=1, color=(52, 52, 52),
                                  thickness=2, position=(30, 30))
        # day_name
        day_name = datetime.date.strftime(self.date, "%A")
        self.image_maker.put_text(text=day_name, font_scale=0.8, color=(52, 52, 52),
                                  thickness=2, position=(30, 55))
        # temperature
        temperature = f'{"Температура:":<12} {self.temperature}'
        self.image_maker.put_text(text=temperature, font_scale=0.5, color=(52, 52, 52),
                                  thickness=1, position=(30, 110))
        # wind
        wind = f'{"Ветер:":<14} {self.wind}'
        self.image_maker.put_text(text=wind, font_scale=0.5, color=(52, 52, 52),
                                  thickness=1, position=(30, 130))
        # humidity
        humidity = f'{"Влажность:":<12} {self.humidity}'
        self.image_maker.put_text(text=humidity, font_scale=0.5, color=(52, 52, 52),
                                  thickness=1, position=(30, 150))

    def _parse_weather(self, weather):
        self.date = weather['date']
        self.temperature = weather['day_temperature']
        self.pressure = weather['pressure']
        self.humidity = weather['humidity']
        self.wind = weather['wind']
        self.day_description = weather['day_description']
        self.icon_type = self.ICON_SETTINGS[self.day_description]['icon']
        self.gradient_color = self.ICON_SETTINGS[self.day_description]['color']


class WeatherCLI(object):

    def __init__(self):
        self.weather_maker = WeatherMaker()
        self.database_updater = DatabaseUpdater()
        self.postcard = PostcardMaker()
        self.today = datetime.date.strftime(datetime.date.today(), '%Y-%m-%d')
        self.week_before = datetime.date.strftime(datetime.date.today() - datetime.timedelta(days=7), '%Y-%m-%d')
        self.write_to_base(from_=self.week_before, to_=self.today)

    def write_to_base(self, from_, to_=None):
        """Write weather data to database

        Params:
            from_(datetime.date) get and write data from YYYY-MM-DD
            to_ (datetime.date) get and write data to YYYY-MM-DD
        """
        parsed_data = self.weather_maker.get_data(period_from=from_, period_to=to_)
        self.database_updater.save_data(parsed_data)

    def load_from_base(self, from_, to_=None):
        weather = self.database_updater.load_data(from_, to_)
        return weather

    def make_postcard(self, from_, to_=None):
        weather = self.load_from_base(from_, to_)

        if not weather:
            self.write_to_base(from_, to_)
            weather = self.load_from_base(from_, to_)

        if 'postcards' not in os.listdir():
            os.makedirs('postcards')

        for i, elem in enumerate(weather):
            img_path = os.path.join('postcards', f'day_{i}.jpg')
            self.postcard.generate_postcard(elem)
            self.postcard.save_image(img_path)


if __name__ == '__main__':
    fire.Fire(WeatherCLI)
