from turtle import *


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("mint cream")
        self.shapesize(stretch_wid=8, stretch_len=0.7)
        self.tilt(90)
        self.penup()
        self.goto(position)
        self.speed(0)

    def go_right(self):
        if self.xcor() < 250:  # 300 - half of paddle width
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -250:  # -300 + half of paddle width
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
