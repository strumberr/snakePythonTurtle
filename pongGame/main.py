import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2



text_turtle1 = turtle.Turtle()
text_turtle1.color('deep pink')
style = ('Courier', 30, 'italic')

text_turtle1.penup()
text_turtle1.goto(-wn.window_width() / 2 + 10, wn.window_height() / 2 - 40)
text_turtle1.pendown()

text_turtle1.write(f'Score', font=style, align='left')
text_turtle1.hideturtle()


text_turtle2 = turtle.Turtle()
text_turtle2.color('deep pink')
style = ('Courier', 30, 'italic')
text_turtle2.penup()
text_turtle2.goto(wn.window_width() / 2 - 200, wn.window_height() / 2 - 40)
text_turtle2.pendown()
text_turtle2.write(f'Score', font=style, align='left')
text_turtle2.hideturtle()


for i in range(-30, 600, 20):
    dash = turtle.Turtle()
    dash.speed(0)
    dash.shape("square")
    dash.color("white")
    dash.penup()
    dash.goto(0, i - 300)
    dash.shapesize(stretch_wid=0.5, stretch_len=0.2)



def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 10
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 10
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 10
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 10
    paddle_b.sety(y)



def paddle_b_up_auto(y):
    paddle_b.sety(y)




paddle_a_speed = 0
paddle_b_speed = 0


def move_paddles():
    global paddle_a_speed, paddle_b_speed

    y_a = paddle_a.ycor()
    y_a += paddle_a_speed
    if -240 <= y_a <= 240:
        paddle_a.sety(y_a)


    y_b = paddle_b.ycor()
    y_b += paddle_b_speed
    if -240 <= y_b <= 240:
        paddle_b.sety(y_b)

    wn.update()
    wn.ontimer(move_paddles, 10)

def set_paddle_speed(paddle, speed):
    global paddle_a_speed, paddle_b_speed
    if paddle == "paddle_a":
        paddle_a_speed = speed
    elif paddle == "paddle_b":
        paddle_b_speed = speed

wn.listen()
wn.onkeypress(lambda: set_paddle_speed("paddle_a", 10), "w")
wn.onkeypress(lambda: set_paddle_speed("paddle_a", -10), "s")
wn.onkeypress(lambda: set_paddle_speed("paddle_b", 10), "Up")
wn.onkeypress(lambda: set_paddle_speed("paddle_b", -10), "Down")

wn.onkey(lambda: set_paddle_speed("paddle_a", 0), "w")
wn.onkey(lambda: set_paddle_speed("paddle_a", 0), "s")
wn.onkey(lambda: set_paddle_speed("paddle_b", 0), "Up")
wn.onkey(lambda: set_paddle_speed("paddle_b", 0), "Down")

move_paddles()


update = 0

counter_points_paddle_a = 0
counter_points_paddle_b = 0

while True:

    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # paddle_b_up_auto(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

        text_turtle1.clear()
        counter_points_paddle_a = 0
        text_turtle1.write(f'0', font=style)

        text_turtle2.clear()
        counter_points_paddle_b = 0
        text_turtle2.write(f'0', font=style)
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

        text_turtle1.clear()
        counter_points_paddle_a = 0
        text_turtle1.write(f'0', font=style)

        text_turtle2.clear()
        counter_points_paddle_b = 0
        text_turtle2.write(f'0', font=style)




    if (paddle_b.xcor() - 20 < ball.xcor() < paddle_b.xcor()) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):

        text_turtle2.clear()
        counter_points_paddle_b += 1
        text_turtle2.write(f'{counter_points_paddle_b}', font=style)

        ball.setx(paddle_b.xcor() - 20)
        ball.dx *= -1

    if (paddle_a.xcor() + 20 > ball.xcor() > paddle_a.xcor()) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):

        text_turtle1.clear()
        counter_points_paddle_a += 1
        text_turtle1.write(f'{counter_points_paddle_a}', font=style)

        ball.setx(paddle_a.xcor() + 20)
        ball.dx *= -1

    update += 1
    print(update)

    
