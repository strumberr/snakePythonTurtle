import turtle
import random

t = turtle.Turtle()

side_length = 100

t.speed(10)

for sides in range(3, 13):
    color = ['#{:02X}{:02X}{:02X}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))][0]
    print(color)
    t.pencolor(color)
    for _ in range(sides):
        t.forward(side_length)
        t.left(360 / sides)

turtle.done()
