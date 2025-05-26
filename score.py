from turtle import Turtle

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0

        self.score_writer = Turtle()
        self.score_writer.color("white")
        self.score_writer.penup()
        self.score_writer.hideturtle()

        self.high_score_writer = Turtle()
        self.high_score_writer.color("white")
        self.high_score_writer.penup()
        self.high_score_writer.hideturtle()

        self.update_score()
        self.update_high_score()

    def update_score(self):
        self.score_writer.clear()
        self.score_writer.goto(-175, 200)
        self.score_writer.write(f"Score: {self.score}", align="center", font=("Courier", 20, "bold"))

    def update_high_score(self):
        self.high_score_writer.clear()
        self.high_score_writer.goto(150, 200)
        self.high_score_writer.write(f"High Score: {self.high_score}", align="center", font=("Courier", 20, "bold"))

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_score()
