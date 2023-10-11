import turtle

class BallMovement():
    def __init__(self, wn):
        self.wn = wn

        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = -2

        self.reset = False

    def ballMechanics(self):

        self.reset = False

        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
    
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1


        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.reset = True


        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.reset = True

        return self.ball.xcor(), self.ball.ycor(), self.ball.dx, self.ball.dy, self.reset
    
    def bounceDX(self):
        self.ball.dx *= -1

    def bounceDY(self):
        self.ball.dy *= -1

    def setBallXPaddleB(self, paddle_b):
        self.ball.setx(paddle_b.xcor() - 20)

    def setBallXPaddleA(self, paddle_a):
        self.ball.setx(paddle_a.xcor() + 20)


