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



class snakeGame():
    def __init__(self, screen, head, food, counter_points, turtle, style, segments, segment_distance):
        self.screen = screen
        self.head = head
        self.food = food
        self.counter_points = counter_points
        self.turtle = turtle
        self.style = style
        self.segments = segments
        self.segment_distance = segment_distance


    # Functions
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def runningMain(self):
        self.screen.listen()
        self.screen.onkey(self.go_up, "w")
        self.screen.onkey(self.go_down, "s")
        self.screen.onkey(self.go_left, "a")
        self.screen.onkey(self.go_right, "d")

        taken_food = False


        while True:
            self.screen.update()


            if self.head.distance(food) < 20:

                print("food taken")


                self.turtle.clear()

                self.counter_points += 1

                self.turtle.write(f'Score - {self.counter_points}', font=style, align='center')

                x = random.randint(-500, 500)
                y = random.randint(-500, 500)

                self.food.goto(x, y)



                self.new_segment = self.turtle.Turtle()
                self.new_segment.speed(0)
                self.new_segment.shape("square")
                self.new_segment.color("green")


                self.new_segment.penup()
                self.segments.append(self.new_segment)

            



            for index in range(len(self.segments) - 1, 0, -1):
                x = self.segments[index - 1].xcor()
                y = self.segments[index - 1].ycor()
                print(x, y)
                self.segments[index].goto(x, y)


            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()


            if self.head.xcor() > 520 or self.head.xcor() < -520 or self.head.ycor() > 480 or self.head.ycor() < -460:

                print("Game Over - reason - hit the wall")

                self.turtle.clear()
                self.counter_points = 0

                self.explosion = self.turtle.Turtle()
                self.explosion.color("yellow")
                self.explosion.pensize(1)
                self.explosion.speed(500)
                self.explosion.hideturtle()

                x, y = self.head.xcor(), self.head.ycor()

                self.explosion.penup()
                self.explosion.goto(x, y)
                self.explosion.pendown()

                for i in range(30):
                    angle = random.randint(0, 45)
                    distance = random.randint(0, 300)
                    self.explosion.right(angle)
                    self.explosion.forward(distance)
                    self.explosion.backward(distance)


                self.head.goto(0, 0)
                self.head.direction = "stop"


                for segment in self.segments:
                    self.segment.goto(1000, 1000)


                self.segments.clear()


            for segment in self.segments:
                if self.head.distance(segment) < 2:
                    print("Game Over - reason - hit itself")

                    self.turtle.clear()
                    self.counter_points = 0

                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"


                    for segment in self.segments:
                        self.segment.goto(1000, 1000)


                    self.segments.clear()


            time.sleep(0.1)



segments = []

segment_distance = 20

snakeGame = snakeGame(screen, head, food, counter_points, turtle, style, segments, segment_distance)

snakeGame.runningMain()
