import simple_draw as sd
def smile(x, y, colors):
  sd.circle(sd.Point(x + 11, y + 11), 6, colors, 1)
  sd.circle(sd.Point(x - 9, y + 11), 6, colors, 1)
  sd.circle(sd.Point(x, y), 30, colors, 1)
  sd.line(sd.Point(x - 6, y - 9), sd.Point(x + 7, y - 9), colors, 1)
  sd.line(sd.Point(x - 6, y - 9), sd.Point(x - 9, y - 6), colors, 1)
  sd.line(sd.Point(x + 7, y - 9), sd.Point(x + 10, y - 6), colors, 1)


def smile1(x, y, colors):
  sd.circle(sd.Point(x + 11, y + 11), 1, colors, 1)
  sd.circle(sd.Point(x - 9, y + 11), 1, colors, 1)
  sd.circle(sd.Point(x, y), 30, colors, 1)
  sd.line(sd.Point(x - 6, y - 9), sd.Point(x + 7, y - 9), colors, 1)
  sd.line(sd.Point(x - 6, y - 9), sd.Point(x - 9, y - 6), colors, 1)
  sd.line(sd.Point(x + 7, y - 9), sd.Point(x + 10, y - 6), colors, 1)