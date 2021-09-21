import turtle

XMAX = 300
XMIN = -XMAX
YMAX = 300
YMIN = -YMAX


def init():
    turtle.reset()
    turtle.goto(XMIN, YMAX)
    return

def draw_black_pixel():
    turtle.speed(0)

init()

