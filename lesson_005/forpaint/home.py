import simple_draw as sd

sd.resolution = [1200, 600]


def house():
    sd.rectangle(sd.Point(0, 0), sd.Point(1200, 50), color=sd.COLOR_WHITE, width=0)  # снежное поле

    sd.rectangle(sd.Point(400, 50), sd.Point(700, 250), width=1)
    delta = 25
    for y in range(50, 250, 20):
        delta += 25
        for x in range(375 + delta, 675, 50):
            if x > 375:
                sd.rectangle(sd.Point(x, y), sd.Point(x + 50, y + 20), width=1)
        delta -= 50






def window_and_roof():


    points_for_roof = [
        sd.Point(350, 250), sd.Point(750, 250), sd.Point(550, 330)
    ]
    sd.lines(points_for_roof, width=0, closed=True)
    sd.rectangle(sd.Point(500, 110), sd.Point(600, 210), width=0)
    sd.polygon(points_for_roof, color=sd.COLOR_RED, width=0)
    sd.square(sd.Point(500, 110), 100, color=sd.COLOR_BLACK, width=4)
