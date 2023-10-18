import turtle
import time
import random
import json 


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

        self.explosion = turtle.Turtle()
        self.explosion.color("yellow")
        self.explosion.pensize(1)
        self.explosion.speed(500)
        self.explosion.hideturtle()

        self.timer = 0
        self.timerStart = False

        self.extra_food = []

        self.obstacles = []
        





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

    def getHighscore(self):
        with open("snakeGame/snakegame.json", "r") as json_file:
            retrieved_data = json.load(json_file)

        return retrieved_data["highscore"]
    
    def getTime(self):
        with open("snakeGame/snakegame.json", "r") as json_file:
            retrieved_data = json.load(json_file)

        return retrieved_data["time"]
    
    def setHighscore(self, highscore):
        with open("snakeGame/snakegame.json", "r") as json_file:
            retrieved_data = json.load(json_file)

        retrieved_data["highscore"] = highscore

        with open("snakeGame/snakegame.json", "w") as json_file:
            json.dump(retrieved_data, json_file)

    def setTime(self, time):
        with open("snakeGame/snakegame.json", "r") as json_file:
            retrieved_data = json.load(json_file)

        retrieved_data["time"] = time

        with open("snakeGame/snakegame.json", "w") as json_file:
            json.dump(retrieved_data, json_file)
    

    def spawn_extra_food(self):
        for _ in range(3):
            extra_food_piece = turtle.Turtle()
            extra_food_piece.speed(0)
            extra_food_piece.shape("circle")
            extra_food_piece.color("red")
            extra_food_piece.penup()
            x = random.randint(-450, 450)
            y = random.randint(-450, 450)
            extra_food_piece.goto(x, y)
            self.extra_food.append(extra_food_piece)
    

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


                if not self.timerStart:
                    self.timer = time.time()
                    self.timerStart = True
                    print("timer started", self.timer)
                

                print("food taken")


                self.turtle.clear()

                self.counter_points += 1

                self.turtle.penup()
                self.turtle.goto(-520, 440)
                self.turtle.write(f'Highscore - {self.getHighscore()}', font=self.style, align='left')

                self.turtle.penup()
                self.turtle.goto(-520, 400)
                self.turtle.write(f'Score - {self.counter_points}', font=self.style, align='left')

                self.turtle.penup()
                self.turtle.goto(-520, 360)
                self.turtle.write(f'Time - {self.getTime()}', font=self.style, align='left')

                x = random.randint(-450, 450)
                y = random.randint(-450, 450)

                self.food.goto(x, y)

                for el in self.obstacles:
                    el.hideturtle()
                self.obstacles = []


                for _ in range(3):
                
                    obstacle = turtle.Turtle()
                    obstacle.speed(0)
                    obstacle.shape("circle")
                    obstacle.color("white")
                    obstacle.shapesize(stretch_wid=2, stretch_len=2)
                    obstacle.penup()
                    x = random.randint(-450, 450)
                    y = random.randint(-450, 450)
                    obstacle.goto(x, y)
                    self.obstacles.append(obstacle)


                self.new_segment = self.turtle.Turtle()
                self.new_segment.speed(0)
                self.new_segment.shape("square")
                self.new_segment.color("green")


                self.new_segment.penup()
                self.segments.append(self.new_segment)

            for extra_food_piece in self.extra_food:
                if self.head.distance(extra_food_piece) < 20:
                    self.extra_food.remove(extra_food_piece)
                    extra_food_piece.hideturtle()

                    self.counter_points += 1
                    self.turtle.clear()
                    
                    self.turtle.penup()
                    self.turtle.goto(-520, 440)
                    self.turtle.write(f'Highscore - {self.getHighscore()}', font=self.style, align='left')

                    self.turtle.penup()
                    self.turtle.goto(-520, 400)
                    self.turtle.write(f'Score - {self.counter_points}', font=self.style, align='left')

                    self.turtle.penup()
                    self.turtle.goto(-520, 360)
                    self.turtle.write(f'Time - {self.getTime()}', font=self.style, align='left')

                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("square")
                    new_segment.color("green")
                    new_segment.penup()
                    self.segments.append(new_segment)


            if len(self.extra_food) < 1:
                self.spawn_extra_food()



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



            for obstacle in self.obstacles:
                if self.head.distance(obstacle) < 25:
                    print("Game Over - reason - hit the obstacle")

                    if self.counter_points > self.getHighscore():
                        timeTimer = time.time() - self.timer
                        minutes = int(timeTimer // 60)
                        seconds = int(timeTimer % 60)
                        self.setTime(f"{minutes}m:{seconds}s")
                        self.timerStart = True
                        print("timer ended", timeTimer)

                    


                    for el in self.obstacles:
                        el.hideturtle()
                    self.obstacles = []

                    for el in self.segments:
                        el.hideturtle()

                    self.segments = []
                    self.new_segment.clear()
                    
                    if self.counter_points > self.getHighscore():
                        self.setHighscore(self.counter_points)

                    self.turtle.clear()
                    self.counter_points = 0

                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"


                    obstacle.hideturtle()


                    self.obstacles.clear()


            if self.head.xcor() > 520 or self.head.xcor() < -520 or self.head.ycor() > 480 or self.head.ycor() < -460:

                print("Game Over - reason - hit the wall")

                if self.counter_points > self.getHighscore():
                    timeTimer = time.time() - self.timer
                    minutes = int(timeTimer // 60)
                    seconds = int(timeTimer % 60)
                    self.setTime(f"{minutes}m:{seconds}s")
                    self.timerStart = True
                    print("timer ended", timeTimer)
        
                for el in self.segments:
                    el.hideturtle()
                self.segments = []
                self.new_segment.clear()

                for el in self.obstacles:
                    el.hideturtle()
                self.obstacles = []




                if self.counter_points > self.getHighscore():
                    self.setHighscore(self.counter_points)


                self.turtle.clear()
                self.counter_points = 0


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
                    segment.hideturtle()


                self.segments.clear()


            for segment in self.segments:
                if self.head.distance(segment) < 2:
                    print("Game Over - reason - hit itself")

                    if self.counter_points > self.getHighscore():
                        timeTimer = time.time() - self.timer
                        minutes = int(timeTimer // 60)
                        seconds = int(timeTimer % 60)
                        self.setTime(f"{minutes}m:{seconds}s")
                        self.timerStart = True
                        print("timer ended", timeTimer)

                    for el in self.obstacles:
                        el.hideturtle()
                    self.obstacles = []

                    for el in self.segments:
                        el.hideturtle()
                    self.segments = []
                    self.new_segment.clear()
                    
                    if self.counter_points > self.getHighscore():
                        self.setHighscore(self.counter_points)

                    self.turtle.clear()
                    self.counter_points = 0

                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"


                    segment.hideturtle()


                    self.segments.clear()


            time.sleep(0.1)



segments = []

segment_distance = 20

snakeGame = snakeGame(screen, head, food, counter_points, turtle, style, segments, segment_distance)

snakeGame.runningMain()
