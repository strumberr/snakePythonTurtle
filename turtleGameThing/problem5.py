import turtle
import random
import math

t = turtle.Turtle()

turtle.bgcolor("black")

t.speed(0)
t.width(2)


R = 100
r = 81
d = 103


def draw_spirograph(R, r, d):

    turn_counter = 0

    theta = 0
    t.penup()
    t.goto(R-r+d*math.cos(math.radians(theta)), d*math.sin(math.radians(theta)))
    t.pendown()
    
    t.color(get_random_color())

    random_color = get_random_color()

    for _ in range(360):
        theta += 1

        if turn_counter <= 3:
            pass
        else:
            random_color = get_random_color()
            t.color(random_color)
            turn_counter = 0

        x = (R - r) * math.cos(math.radians(theta)) + d * math.cos((R - r) * theta / r)
        y = (R - r) * math.sin(math.radians(theta)) - d * math.sin((R - r) * theta / r)
        t.goto(x, y)
        t.color(random_color)
        turn_counter += 1


def get_random_color():
    return ['#{:02X}{:02X}{:02X}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))][0]


draw_spirograph(R, r, d)

turtle.done()
