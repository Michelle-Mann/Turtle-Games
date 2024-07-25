# Name: Michelle Mann
# Project Name: Turtle Snake Game - Food
# Date: 8/28/2023
# Description: 100 Days of Code (Day 18-22) by: The App Brewery.
# Code below details how the scoreboard object will work.

from turtle import Turtle
import random


class Food(Turtle):
    """
    Defines a Food object. Food objects are a single turtle segment to in the color blue.
    Food objects are created randomly in different locations across the playable
    screen.

    This class has built-in methods for the following:
    - Refreshing a new placement of a food object.
    """

    def __init__(self):
        """A food object is a 10x10 blue circle"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Finds a new x coordinate and y coordinate and sets the new food object there
        before drawing.
        """
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)