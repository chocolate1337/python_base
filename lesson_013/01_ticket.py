# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont, ImageColor



# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_ , to, data):
    image = os.path.join('images', 'ticket_template.png')
    fonts = os.path.join('fonts', 'ofont.ru_Cyntho Next Slab.ttf')
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(fonts, size=20)
    w, h = im.size
    draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 260), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((260, 260), data, font=font, fill=ImageColor.colormap['black'])
    im.save('probe.png')
    print(f'Post card saved az probe.png')

if __name__ == '__main__':
    make_ticket(fio='Бысев В.В',from_='Australia',to='New Zeuland', data='22.10.2020')
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
