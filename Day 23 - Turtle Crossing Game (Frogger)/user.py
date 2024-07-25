from turtle import Turtle

# Constants
HOME_X = 0                  # Turtle's home position (x-coordinate)
HOME_Y = -280               # Turtle's home position (y-coordinate)
HEAD = 90                   # Turtle's home orientation (pointing up)
FINISH_Y = 280              # Where the end of the level is.

STANDARD_MOVE = 10          # Turtle's default step forward.


class User(Turtle):
    """
    Creation of a literal turtle (player) object. Turtle player can move in the up
    direction only and must avoid all cars on its path to the top of the level.

     This class has built-in methods for the following:
    - Moving the turtle player upwards
    - Resetting the turtle player object to its home position when a level is complete.
    """
    def __init__(self):
        super().__init__()

        # Aesthetics: Turtle object is turtle-shaped, with a upward heading and in white.
        self.shape("turtle")
        self.setheading(HEAD)
        self.color("white")
        self.penup()

        # Placement: Default is bottom of the screen, and centered.
        self.goto(HOME_X, HOME_Y)

    def up(self):
        """
        Defines the ability for our turtle player object to move upward across the screen.
        """
        if self.ycor() < 280:
            self.forward(STANDARD_MOVE)

    def go_home(self):
        """
        Defines the ability of our turtle player object being reset to the bottom of
        the screen.
        """
        self.goto(HOME_X, HOME_Y)
