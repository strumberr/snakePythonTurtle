import turtle
import random
from ball import BallMovement

class Obstacle(turtle.Turtle):
    def __init__(self, wn):
        super().__init__()

        self.wn = wn

        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.random_x = random.randint(-260, 260)
        self.random_y = random.randint(-260, 260)
        self.goto(self.random_x, self.random_y)

        self.dx = 2
        self.dy = -2


    def obstacleCollision(self, ball):
        self.ballX = ball.xcor()
        self.ballY = ball.ycor()

        #check if ball is near the position as the obstacle:

        if self.ballX >= self.random_x - 20 and self.ballX <= self.random_x + 20:
            if self.ballY >= self.random_y - 20 and self.ballY <= self.random_y + 20:
                self.dx *= -1
                self.dy *= -1
                self.goto(self.random_x, self.random_y)

                # print(self.ballX, self.ballY)

        # print(self.ballX, self.ballY)

    
    def bounceDX(self):
        self.ball.dx *= -1

    def bounceDY(self):
        self.ball.dy *= -1

    def setBallXPaddleB(self, paddle_b):
        self.ball.setx(paddle_b.xcor() - 20)

    def setBallXPaddleA(self, paddle_a):
        self.ball.setx(paddle_a.xcor() + 20)

        
