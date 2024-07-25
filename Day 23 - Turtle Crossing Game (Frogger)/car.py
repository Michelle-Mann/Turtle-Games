from turtle import Turtle
import random

# Constants
HEAD = 180                          # The heading of our car objects

# A list of colors our car objects can be. We choose a random color for each car.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

PAD_W = 1                           # The default width of a car object
PAD_H = 2                           # The default height of a car object


class Car(Turtle):
    """
    Creation of a car object. Cars are randomly created a various y-positions on the
    right-most side of the screen. Each car is a randomly chosen color.

     This class only defines the initialization of a car object and has no other methods.
    """

    def __init__(self):
        super().__init__()

        # Aesthetics: Cars are stretched square object of random color.
        self.shape("square")
        self.shapesize(stretch_wid=PAD_W, stretch_len=PAD_H, outline=None)
        self.color(random.choice(COLORS))
        self.penup()

        # Sets the car at a random y-coord.
        self.goto(300, random.randint(-250, 250))



