import turtle
import random
from multiprocessing import Pool

def mainExtra(x):


    t = turtle.Turtle()
    t2 = turtle.Turtle()

    shape_array = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

    step_length = 20

    def get_random_color():
        return ['#{:02X}{:02X}{:02X}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))][0]

    t.speed(0)

    for _ in range(1000):
        random_shape = shape_array[random.randint(0, len(shape_array) - 1)]
        t.shape(random_shape)

        turtle.bgcolor(get_random_color())

        t.shapesize(random.randint(1, 2)/1)

        t.pensize(random.randint(1, 10))
        t.color(get_random_color())
        t.forward(step_length)
        random_angle = [90, 180, -90, 0][random.randint(0, 3)]
        t.setheading(random_angle)


        t2.shape(random_shape)
        t2.shapesize(random.randint(1, 2)/1)
        t2.pensize(random.randint(1, 10))
        t2.color(get_random_color())
        t2.forward(step_length)
        random_angle = [90, 180, -90, 0][random.randint(0, 3)]
        t2.setheading(random_angle)
        


    turtle.done()

def mainExtra2(x):


    t = turtle.Turtle()
    t2 = turtle.Turtle()

    shape_array = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

    step_length = 20

    def get_random_color():
        return ['#{:02X}{:02X}{:02X}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))][0]

    t.speed(0)

    for _ in range(1000):
        random_shape = shape_array[random.randint(0, len(shape_array) - 1)]
        t.shape(random_shape)

        turtle.bgcolor(get_random_color())

        t.shapesize(random.randint(1, 2)/1)

        t.pensize(random.randint(1, 10))
        t.color(get_random_color())
        t.forward(step_length)
        random_angle = [90, 180, -90, 0][random.randint(0, 3)]
        t.setheading(random_angle)


        t2.shape(random_shape)
        t2.shapesize(random.randint(1, 2)/1)
        t2.pensize(random.randint(1, 10))
        t2.color(get_random_color())
        t2.forward(step_length)
        random_angle = [90, 180, -90, 0][random.randint(0, 3)]
        t2.setheading(random_angle)
        


    turtle.done()


def main(x):
    mainExtra(x)
    mainExtra2(x)


if __name__ == '__main__':
    with Pool(2) as p:
        print(p.map(main, [1, 2, 3]))