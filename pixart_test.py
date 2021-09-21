import pixart
import turtle

def test_init():
    pixart.init()

    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor()
    assert(x==-270)

def draw_black_pixel_test():
    pixart.draw_black_pixel()
    s=turtle.speed()
    assert(s==0)

    fillcolor=turtle.fillcolor()
    assert(fillcolor=='black')

draw_black_pixel_test()
test_init()