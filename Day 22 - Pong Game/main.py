# Name: Michelle Mann
# Project Name: Pong Game (Created with Turtle)
# Date: 8/28/2023
# Description: 100 Days of Code (Day 22) by: The App Brewery.
# This is a 600 x 800p Turtle adaptation of the mobile classic, Pong. Two paddles will be
# created that hit a ping-pong ball back-and-forth. A two-person game, this allows collaborative
# play of two users at the same keyboard. When a user misses the ball, the opposing user gains a
# point. Users will have the ability to dictate how many scores constitutes as a"win".

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creation of our screen (600 x 800p, black, with a unique title):
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Two-Player Pong Game!")
screen.tracer(0)

# Creation of our objects:
l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

# Play the game:
game_is_on = True

# Prompts how many rounds is considered winner.
win_score = screen.numinput(title="How many rounds?",
                            prompt="# of Rounds to Win?",
                            default=5,
                            minval=1,
                            maxval=21)

# Event Listeners:
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision w/ wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and \
            ball.xcor() < -320:
        ball.bounce_x()

    # Detect miss by r_paddle:
    if ball.xcor() > 380:
        scoreboard.l_point()
        if scoreboard.l_score != win_score:
            ball.reset_position()
            ball.move_speed = 0.1
        else:
            game_is_on = False
            scoreboard.game_over()

    # Detect miss by l_paddle:
    if ball.xcor() < -380:
        scoreboard.r_point()
        if scoreboard.r_score != win_score:
            ball.reset_position()
            ball.move_speed = 0.1
        else:
            game_is_on = False
            scoreboard.game_over()

# Closes the screen
screen.exitonclick()
