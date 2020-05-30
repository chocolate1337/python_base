# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def geometry(point, length,angle_cnt=3, colors=sd.COLOR_YELLOW):
  points = {
      angle_cnt==3:point,
      angle_cnt==4:sd.Point(500,100),
      angle_cnt==5:sd.Point(200,300),
      angle_cnt==6:sd.Point(500,300),
  }
  #point = points[True]
  if colors not in sd.COLOR_YELLOW:
      colors.__add__(colors)
  angle = 0
  for count in range(0,angle_cnt,1):
    v = sd.Vector(start_point=point,length=length,direction=sd._to_radians(angle))
    if count == angle_cnt-1:
        point1 = sd.Point(point.x+length+1, point.y+1)
        sd.line(point, point1)
        break
    v.rotate(sd._to_radians(360 / angle_cnt + count * (360 / angle_cnt)))
    point = v.end_point
    v.draw(color=colors)
  angle_cnt+=1
  if angle_cnt>6:
      return




geometry_text = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']
print('Возможные фигуры:')
for i in enumerate(geometry_text):
    print(f'      {i[0] + 1} : {i[1]}')
while True:
    cnt = input('Введите номер желаемой фигуры > ')
    cnt = int(cnt)
    if (cnt > 5):
        print('Не верный номер!')
    else:
        break
geometry(sd.Point(300,250),100,angle_cnt=cnt+2)



sd.pause()
