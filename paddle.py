from turtle import Turtle

class Paddle(Turtle):
    up_hold = False
    down_hold = False

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(position)



    # Will optimize the holding down the key later

    def pad_up(self):
        # global up_hold
        # up_hold = True
        # if not down_hold:
        # while up_hold:
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    # def pad_up_release():
    #     global up_hold
    #     up_hold = False

    def pad_down(self):
        # global down_hold
        # down_hold = True
        # if not up_hold:
        # while down_hold:
        if -250 < self.ycor():
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
    # def pad_down_release():
    #     global down_hold
    #     down_hold = False
