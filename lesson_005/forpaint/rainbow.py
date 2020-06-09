import simple_draw as sd

sd.resolution = [1200, 600]


def rainbow():
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    radius = 750

    for _ in rainbow_colors:
        color = rainbow_colors[sd.random_number(0, 6)]
        sd.circle(sd.Point(350, 50), radius, color, 20)
        radius += 20
