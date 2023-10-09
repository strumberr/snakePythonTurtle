import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

Toby = turtle.Turtle()
Toby.color("white")
Toby.pensize(1)
Toby.speed(2000)
Toby.hideturtle()

x, y = 90, 100
Toby.penup()
Toby.goto(x, y)
Toby.pendown()


for i in range(20):
    angle = random.randint(0, 45)
    distance = random.randint(0, 150)
    Toby.right(angle)
    Toby.forward(distance)
    Toby.backward(distance)