import simple_draw as sd

sd.resolution = [1200, 600]


def rainbow():
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    r = 750
    # TODO если не используешь переменную, например s, то можно указывать _ Также нейминг подправь пожалуйста,
    #  чтобы переменные отражали то, что они содержат
    for s in rainbow_colors:
        s = rainbow_colors[sd.random_number(0, 6)]
        sd.circle(sd.Point(350, 50), r, s, 20)
        r += 20
