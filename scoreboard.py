from turtle import Turtle
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreR1 = 0
        self.scoreL2 = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.scoreL2, align="center", font=FONT)
        self.goto(100,200)
        self.write(self.scoreR1, align="center", font=FONT)

    def left_point(self):
        self.scoreL2 += 1
        self.update()

    def right_point(self):
        self.scoreR1 += 1
        self.update()
