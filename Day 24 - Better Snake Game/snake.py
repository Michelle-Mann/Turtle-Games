# Name: Michelle Mann
# Project Name: Turtle Snake Game - Snake Object
# Date: 8/28/2023
# Description: 100 Days of Code (Day 18-22) by: The App Brewery.
# Code below details how the snake object will work.

from turtle import Turtle

# CONSTANTS
START_POS = [(0, 0), (-20, 0), (-40, 0)]            # Positions of first three segments
MOVE_DIS = 20                                       # For every move, move 20p
UP = 90                                             # Degree of rotation for "UP"
DOWN = 270                                          # Degree of rotation for "DOWN"
RIGHT = 0                                           # Degree of rotation for "RIGHT"
LEFT = 180                                          # Degree of rotation for "LEFT"


class Snake:
    """
    Defines a Snake object. Snake objects are a collection of 3 @ 20x20 turtle segments to
    start with a designation of "head". Users control the movement of the head segment
    exclusively. The head object must never touch any other segment or a wall.

    This class has built-in methods for the following:
    - Creating a snake object.
    - Adding additional segments.
    - Resetting the Snake object upon end of game.
    - Moving.
    - Event listeners for Up, Down, Left and Right
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates a snake object from scratch. Uses three segments defined as constants
        as initial positions and adds them to our segment list.
        """
        # Creation of a three-segment snake.
        for position in START_POS:
            self.add_seg(position)

    def add_seg(self, position):
        """
        Adds a new snake segment to our array of segments when snake eats food. Uses position
        of last snake segment for starting position of new snake segment. Snake segments are
        new Turtle objects.

        :param position: The position (x, y) coordinate of snake segment.
        :return: None
        """
        # Creation of new turtle object at position.
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)

        # Appending new object to our list of segments.
        self.segments.append(new_segment)

    def reset(self):
        """
        Reset protocol at end of gameplay. Sends snake object to off-screen snake
        graveyard, creates a new snake object re-points the head of snake to this new
        snake object's first segment.
        """
        # Snake graveyard offscreen.
        for seg in self.segments:
            seg.goto(1000, 1000)

        # Clears all segments, creates a new snake and repoints head.
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """
        Extends snake object by creating a new segment and adding it to our snake array.
        """
        # Adds a new segment to the snake.
        self.add_seg(self.segments[-1].position())

    def move(self):
        """
        Moves the snake. Takes each segment after head and moves it to the position of its
        previous segment. Moves the head forward.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DIS)

    def up(self):
        """
        Controls moving the snake upward.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Controls moving the snake downward.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Controls moving the snake to the left.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Controls moving the snake to the right.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
