import turtle
import time
import random



screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=1080, height=1080)
screen.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")



head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")

food.color("red")
food.penup()
food.goto(0, 100)

counter_points = 0

turtle.color('deep pink')
style = ('Courier', 30, 'italic')
turtle.write(f'Score - 0', font=style, align='center')
turtle.hideturtle()


segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

taken_food = False


while True:
    screen.update()


    if head.distance(food) < 20:

        print("food taken")

        #reset the text to update the score
        turtle.clear()


        counter_points += 1

        turtle.write(f'Score - {counter_points}', font=style, align='center')

        x = random.randint(-540, 540)
        y = random.randint(-540, 540)
        food.goto(x, y)


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    



    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    if head.xcor() > 520 or head.xcor() < -520 or head.ycor() > 480 or head.ycor() < -460:

        turtle.clear()
        counter_points = 0

        explosion = turtle.Turtle()
        explosion.color("yellow")
        explosion.pensize(1)
        explosion.speed(500)
        explosion.hideturtle()

        x, y = head.xcor(), head.ycor()

        explosion.penup()
        explosion.goto(x, y)
        explosion.pendown()

        for i in range(30):
            angle = random.randint(0, 45)
            distance = random.randint(0, 300)
            explosion.right(angle)
            explosion.forward(distance)
            explosion.backward(distance)


        head.goto(0, 0)
        head.direction = "stop"


        for segment in segments:
            segment.goto(1000, 1000)


        segments.clear()


    for segment in segments:
        if head.distance(segment) < 20:

            turtle.clear()
            counter_points = 0

            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


            for segment in segments:
                segment.goto(1000, 1000)


            segments.clear()

    time.sleep(0.08)
