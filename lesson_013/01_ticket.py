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

numbers = '1234567890'


class Photo:

    def __init__(self, to, out, date, fio):
        self.date = date
        self.fio = fio
        self.to = to
        self.out = out

    def validate(self):
        self.v_data()
        self.v_fio()
        self.make_ticket()

    def v_data(self):

        valid_date = datetime.strptime(self.date, '%d.%m.%Y')
        now = datetime.now()
        if valid_date < now:
            parser.error('-d не верная дата')

    def v_fio(self):
        for number in numbers:
            if number in self.fio:
                parser.error('-fio маска Фамилия И.О')


    def make_ticket(self):
        # TODO супер, теперь сделай файл с сеттингсами, можно просто файл settings.py, в котором будут глобальные 
        #  переменные капсом, и тут их подтягивай. Это для того, чтобы можно было залезть в цивилизованный 
        #  файл настроик и изменить какие-то параметры, шрифт под хеллоуин итд.)
        image = os.path.join('images', 'ticket_template.png')
        fonts = os.path.join('fonts', 'ofont.ru_Cyntho Next Slab.ttf')
        im = Image.open(image)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(fonts, size=20)
        draw.text((45, 120), self.fio, font=font, fill=ImageColor.colormap['black'])
        draw.text((45, 190), self.out, font=font, fill=ImageColor.colormap['black'])
        draw.text((45, 260), self.to, font=font, fill=ImageColor.colormap['black'])
        draw.text((260, 260), self.date, font=font, fill=ImageColor.colormap['black'])
        im.save('probe.png')
        print(f'Post card saved az probe.png')


parser = argparse.ArgumentParser(description='Заполнение билета')
parser.add_argument('-fio', '--fio', type=str, help='ФИО')
parser.add_argument('-fr', '--fr', type=str, help='Откуда летим')
parser.add_argument('-to', '--to', type=str, help='Куда летим')
parser.add_argument('-d', '--date', type=str, help='Когда летим')
args = parser.parse_args()


if __name__ == '__main__':
    photo = Photo(date=args.date, fio=args.fio, to=args.to, out=args.fr)
    photo.validate()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
