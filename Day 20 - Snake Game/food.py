# Name: Michelle Mann
# Project Name: Turtle Snake Game - Food
# Date: 8/28/2023
# Description: 100 Days of Code (Day 18-22) by: The App Brewery.
# Code below details how the scoreboard object will work.

from turtle import Turtle
import random


class Food(Turtle):

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
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)