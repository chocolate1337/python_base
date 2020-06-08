import simple_draw as sd


def branch(point, angle, length):
    if length < 5:
        return
    delta_random = sd.random_number(-14, 14)
    vector = sd.Vector(point, angle, length)
    vector.draw(width=2, color=sd.COLOR_GREEN)
    coif_length = sd.random_number(-12, 12)
    coif_length = 75 + coif_length
    next_length = length * float(coif_length / 100)
    branch(vector.end_point, angle - 30 - delta_random, next_length)
    branch(vector.end_point, angle + 30 + delta_random, next_length)
