import turtle
from paddles import Paddles
from ball import BallMovement
from score import ScoreTrack
from obstacle import Obstacle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle = Paddles(wn, automatic=True)
paddle.runningMain()
paddle_a = paddle.paddleA()
paddle_b = paddle.paddleB()

BallMovement = BallMovement(wn)
ball = BallMovement.Ball()

score = ScoreTrack(wn)

Obstacle = Obstacle(wn)

while True:
    wn.update()

    paddle.paddle_b_up_auto(ball.ycor() + ball.dy)

    resetGame = BallMovement.ballMechanics()

    paddleAHit = paddle.paddleAHit(paddle_a, ball)
    paddleBHit = paddle.paddleBHit(paddle_b, ball)
    
    if paddleAHit:
        score.scorePlusPaddleA()
        BallMovement.setBallXPaddleA(paddle_a)
        BallMovement.bounceDX()

    if paddleBHit:
        score.scorePlusPaddleB()
        BallMovement.setBallXPaddleB(paddle_b)
        BallMovement.bounceDX()

    if Obstacle.obstacleCollision(ball):
        BallMovement.bounceDX()
        BallMovement.bounceDY()

    if resetGame:
        score.scoreReset()