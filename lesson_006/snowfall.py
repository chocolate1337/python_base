import simple_draw as sd
global number_flakes

sd.resolution = [600,600]
points = []
def random_Point():
    return sd.Point(sd.random_number(50,600),sd.random_number(500,600))



def point_xy(number_flakes):
    for _ in range(number_flakes):
        points.append(random_Point())



def color_flake(points,color):
    for point in points:
        sd.snowflake(point,50,color)


def move(points,number_flakes):
    cnt=0
    for point in points:
        point.y -=10
        point.x += sd.random_number(-10,10)
        if point.y<0:
            cnt+=1
            print(f'Снежинка под номером {cnt} упала')
            if cnt == number_flakes:
                points.clear()
                point_xy(number_flakes)









