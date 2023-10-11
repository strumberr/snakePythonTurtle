import turtle

class Paddles():
    def __init__(self, wn, automatic=False):

        self.wn = wn
        self.paddle_a = turtle.Turtle()
        self.paddle_b = turtle.Turtle()
        self.paddle_a_speed = 0
        self.paddle_b_speed = 0
        self.automatic = automatic

        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-350, 0)

        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(350, 0)



    def paddle_b_up_auto(self, y):
        if self.automatic:
            self.paddle_b.sety(y)
        else:
            pass


    def move_paddles(self):

        y_a = self.paddle_a.ycor()
        y_a += self.paddle_a_speed
        if -240 <= y_a <= 240:
            self.paddle_a.sety(y_a)


        y_b = self.paddle_b.ycor()
        y_b += self.paddle_b_speed
        if -240 <= y_b <= 240:
            self.paddle_b.sety(y_b)

        self.wn.update()
        self.wn.ontimer(self.move_paddles, 10)

    def set_paddle_speed(self, paddle, speed):

        if paddle == "paddle_a":
            self.paddle_a_speed = speed
        elif paddle == "paddle_b":
            self.paddle_b_speed = speed

    def runningMain(self):
        self.wn.listen()
        self.wn.onkeypress(lambda: self.set_paddle_speed("paddle_a", 10), "w")
        self.wn.onkeypress(lambda: self.set_paddle_speed("paddle_a", -10), "s")
        self.wn.onkeypress(lambda: self.set_paddle_speed("paddle_b", 10), "Up")
        self.wn.onkeypress(lambda: self.set_paddle_speed("paddle_b", -10), "Down")

        self.wn.onkey(lambda: self.set_paddle_speed("paddle_a", 0), "w")
        self.wn.onkey(lambda: self.set_paddle_speed("paddle_a", 0), "s")
        self.wn.onkey(lambda: self.set_paddle_speed("paddle_b", 0), "Up")
        self.wn.onkey(lambda: self.set_paddle_speed("paddle_b", 0), "Down")

        self.move_paddles()

    def paddleA(self):

        return self.paddle_a
    
    def paddleB(self):
        return self.paddle_b
    
    
    def paddleAHit(self, paddle_a, ball):
        if (paddle_a.xcor() + 20 > ball.xcor() > paddle_a.xcor()) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            return True
        else:
            return False
        
    def paddleBHit(self, paddle_b, ball):
        if (paddle_b.xcor() - 20 < ball.xcor() < paddle_b.xcor()) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            return True
        else:
            return False