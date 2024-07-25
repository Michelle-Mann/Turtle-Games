# Name: Michelle Mann
# Project Name: Turtle Capstone Project (Turtle Crossings: Frogger)
# Date: 8/30/2023
# Description: 100 Days of Code (Day 23) by: The App Brewery.
# This is a 600 x 600p Turtle adaptation of the mobile classic, Frogger. Our turtle will attempt
# to cross a busy "road" from the bottom of our window to the top without hitting "car" objects.
# The speed by which the cars move will steadily increase as the levels become more difficult.

from turtle import Screen
from user import User
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Creation of our screen (600 x 600p, black, with a unique title):
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossings!")
screen.tracer(0)

# Creation of our objects:
turtle = User()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.update()

# Event Listeners:
screen.listen()
screen.onkey(turtle.up, "Up")

# Play the game:
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car:
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect halfway point after new level:
    if turtle.ycor() == -200 and scoreboard.level >= 2:
        scoreboard.update_scoreboard()

    # Detect if turtle has successfully made it to top:
    if turtle.ycor() > 250:
        scoreboard.new_level()
        car_manager.level_up()
        turtle.go_home()

# Closes the screen
screen.exitonclick()
