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

# Set's Up Screen (600 x 600). Screen should have a title and will use tracer with update to
# facilitate game play animation.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Initializes game by creating all objects:
scoreboard = Scoreboard()
snake = Snake()
food = Food()

game_is_on = True

# Game play.
# __________________________


def new_game():
    """
    Prompts the player at the end of a collision if they want to play again via
    a pop-up window. If "Y" restarts gameplay, if "N" closes the screen.
    """
    # Pop-up window with input.
    play_again = screen.textinput(title="Play Again!?",
                                  prompt="Type 'Y' for Yes and 'N' for No:"
                                  )

    # Resets snake structure and scoreboard on yes. Exits on no.
    if play_again.lower() == "y":
        scoreboard.reset()
        snake.reset()
        play_game()
    else:
        screen.bye()


def play_game():
    """
    All aspects of game play. Establishes keyboard listeners, and a movement loop for snake
    object. While the game is on, moves the snake object and determines if a collision has
    happened.
    """
    # Development of our keyboard listeners. Users will play with up, down, left and right arrow
    # keys to move the head of the snake.
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Movement while loop. Refreshes screen and moves snake.
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
            new_game()

        # Detect collision with self
        for segment in snake.segments[1::]:
            if snake.head.distance(segment) < 10:
                new_game()


# Initializes game play.
play_game()

# Closes the screen
screen.exitonclick()
