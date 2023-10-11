import turtle
from paddles import Paddles
from ball import BallMovement
from score import ScoreTrack

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle = Paddles(wn, automatic=True)
paddle.runningMain()
paddle_a = paddle.paddleA()
paddle_b = paddle.paddleB()

ballClass = BallMovement(wn)
ball = BallMovement(wn).ball

score = ScoreTrack(wn)

update = 0

while True:
    wn.update()

    paddle.paddle_b_up_auto(ball.ycor() + ball.dy)

    ball = ballClass.ball

    ballX, ballY, ballDX, ballDY, reset = ballClass.ballMechanics()

    paddleAHit = paddle.paddleAHit(paddle_a, ball)
    paddleBHit = paddle.paddleBHit(paddle_b, ball)
    
    if paddleAHit:
        score.scorePlusPaddleA()
        ballClass.setBallXPaddleA(paddle_a)
        ballClass.bounceDX()

    if paddleBHit:
        score.scorePlusPaddleB()
        ballClass.setBallXPaddleB(paddle_b)
        ballClass.bounceDX()

    if reset:
        score.scoreReset()