from turtle import Screen
from paddle import Paddle
from brick import Brick
from ball import Ball
import time
from tkinter import messagebox
from score import Score


# Objects
screen = Screen()
paddle = Paddle((0, -220))
ball = Ball((0, -10))
user_score = Score()


# Screen setup
screen.bgcolor("black")
screen.setup(width=600, height=500)
screen.title("Brick Breakker")
screen.tracer(0)


# Brick setup
bricks = []


def create_bricks():
    start_x = -275
    start_y = 150
    gap = 45
    bricks_per_row = 13
    rows = 7
    colors = ["red", "teal", "gold",  "spring green", "dark violet", "cyan", "magenta"]

    for row in range(rows):
        y = start_y - (row * 25)
        for i in range(bricks_per_row):
            x = start_x + (i * gap)
            brick = Brick((x, y))
            brick.color(colors[row % len(colors)])
            bricks.append(brick)


create_bricks()

# Controls
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


def start_game():
    game_is_on = True

    while game_is_on:
        time.sleep(0.05)
        screen.update()
        ball.move()

        for brick in bricks[:]:  # Use a copy to avoid modifying list while iterating
            if abs(ball.xcor() - brick.xcor()) < 25 and abs(ball.ycor() - brick.ycor()) < 15:
                brick.hideturtle()
                bricks.remove(brick)
                ball.bounce_y()
                user_score.add_score()

        # Detect collisions with top wall
        if ball.ycor() > 230:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.ycor() < -200 and abs(ball.xcor() - paddle.xcor()) < 50:
            ball.bounce_y()

        # Detect collisions with left and right walls
        if ball.xcor() > 280 or ball.xcor() < -280:
            ball.bounce_x()

        # Detect ball falling below paddle
        if ball.ycor() < -230:
            game_is_on = False
            answer = messagebox.askyesno("Game Over", "Game Over! Want to play again?")
            if answer:
                # Reset ball, paddle and score
                ball.goto(0, -10)
                ball.dx = 3
                ball.dy = 3
                paddle.goto(0, -220)
                user_score.reset_score()

                # Clear old bricks
                for brick in bricks:
                    brick.hideturtle()
                bricks.clear()

                # Create new bricks and restart game
                create_bricks()
                start_game()
            else:
                screen.bye()


start_game()


screen.exitonclick()
