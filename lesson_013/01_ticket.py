# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse
from datetime import datetime

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


parser = argparse.ArgumentParser(description='Заполнение билета')
parser.add_argument('-fio','--fio',type=str,help='ФИО')
parser.add_argument('-fr','--fr',type=str,help='Откуда летим')
parser.add_argument('-to','--to',type=str,help='Куда летим')
parser.add_argument('-d','--date', type=str, help='Когда летим')
args = parser.parse_args()
numbers = '1234567890'

class Validation:

    def __init__(self, date, fio):
        self.date = date
        self.fio = fio

    def validate(self):
        self.v_data()
        self.v_fio()

    def v_data(self):

        valid_date = datetime.strptime(self.date, '%d.%m.%Y')
        now = datetime.now()
        if valid_date < now:
            parser.error('-d не верная дата')


    def v_fio(self):
        for number in numbers:
            if number in self.fio:
                parser.error('-fio маска Фамилия И.О')
# TODO тут по кодингстайлу сначала идут классы/ф-ии потом код, который с ними работает.
valid = Validation(date=args.date,fio=args.fio)
valid.validate()

# TODO почему бы не создать класс с атрибутами полей билета и методами получить билет итд? Также можно создать файл сеттингсов с шрифтом и тд, и оттуда подтягивать данные
def make_ticket(fio, from_ , to, data):
    image = os.path.join('images', 'ticket_template.png')
    fonts = os.path.join('fonts', 'ofont.ru_Cyntho Next Slab.ttf')
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(fonts, size=20)
    draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 260), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((260, 260), data, font=font, fill=ImageColor.colormap['black'])
    im.save('probe.png')
    print(f'Post card saved az probe.png')

if __name__ == '__main__':
    make_ticket(fio=args.fio, from_=args.fr, to=args.to, data=args.date)


# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
