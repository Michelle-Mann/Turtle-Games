# Name: Michelle Mann
# Project Name: Turtle Snake Game
# Date: 8/28/2023
# Description: 100 Days of Code (Day 18-22) by: The App Brewery.
# This is a 600 x 600p Turtle adaptation of the mobile classic, Snake. Snake begins with
# 3 x 20p square and attempts to collect food without colliding with self or outside edge.
# User can use up, down, left and right keys in order to move snake object. Snake object
# grows with every new food it obtains!

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set's Up Screen (600 x 600)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Initializes game by creating all objects:
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# Development of our keyboard listeners. Users will play with
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake!
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 \
            or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with self
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Closes the screen
screen.exitonclick()
