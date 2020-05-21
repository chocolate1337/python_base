# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


geometry_text = ['Треугольник','Квадрат','Пятиугольник','Шестиугольник']
print('Возможные фигуры:')
for i in enumerate(geometry_text):
    print(f'      {i[0]+1} : {i[1]}')
while True:
    cnt = input('Введите номер желаемой фигуры > ')
    cnt= int(cnt)
    if(cnt > 4):
        print('Не верный номер!')
    else:
        break;
def geometry(point,angle,length,*args):
    point_1 = point
    for count in args[0]:
         v = sd.get_vector(point, angle + count, length=length)
         point = v.end_point
         v.draw()
    sd.line(point_1,point)
if cnt == 1:
    geometry(sd.get_point(250,250),0,100,[0,120,240])
elif cnt==2: geometry(sd.get_point(250,250),0,100,[0,90,180,270])
elif cnt==3: geometry(sd.get_point(250,250),0,100,[0,72,144,216,288])
elif cnt==4: geometry(sd.get_point(250,250),0,100,[0,60,120,180,240,300])



sd.pause()
