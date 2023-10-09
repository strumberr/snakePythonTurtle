import turtle

t = turtle.Turtle()

t.pensize(2)
t.pencolor("blue")

for _ in range(10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

turtle.done()