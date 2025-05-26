from turtle import *


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.tilt(90)
        self.penup()
        self.goto(position)
