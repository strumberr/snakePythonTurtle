import turtle

class ScoreTrack():
    def __init__(self, wn):
        self.style = ('Courier', 30, 'italic')

        self.score_turtle1 = 0
        self.score_turtle2 = 0

        self.text_turtle1 = turtle.Turtle()
        self.text_turtle1.color('deep pink')

        self.text_turtle1.penup()
        self.text_turtle1.goto(-wn.window_width() / 2 + 10, wn.window_height() / 2 - 40)
        self.text_turtle1.pendown()

        self.text_turtle1.write(f'Score', font=self.style, align='left')
        self.text_turtle1.hideturtle()


        self.text_turtle2 = turtle.Turtle()
        self.text_turtle2.color('deep pink')
        self.text_turtle2.penup()
        self.text_turtle2.goto(wn.window_width() / 2 - 200, wn.window_height() / 2 - 40)
        self.text_turtle2.pendown()
        self.text_turtle2.write(f'Score', font=self.style, align='left')
        self.text_turtle2.hideturtle()

        for i in range(-30, 600, 20):
            self.dash = turtle.Turtle()
            self.dash.speed(0)
            self.dash.shape("square")
            self.dash.color("white")
            self.dash.penup()
            self.dash.goto(0, i - 300)
            self.dash.shapesize(stretch_wid=0.5, stretch_len=0.2)

    def textOne(self):
        return self.text_turtle1
    
    def textTwo(self):
        return self.text_turtle2
    

    def scorePlusPaddleA(self):
    
        self.text_turtle1.clear()
        self.score_turtle1 += 1
        self.text_turtle1.write(f'{self.score_turtle1}', font=self.style)


    def scorePlusPaddleB(self):

        self.text_turtle2.clear()
        self.score_turtle2 += 1
        self.text_turtle2.write(f'{self.score_turtle2}', font=self.style)

    def scoreReset(self):
    
        self.text_turtle1.clear()
        self.score_turtle1 = 0
        self.text_turtle1.write(f'0', font=self.style)

        self.text_turtle2.clear()
        self.score_turtle2 = 0
        self.text_turtle2.write(f'0', font=self.style)

        return self.score_turtle1, self.score_turtle2
