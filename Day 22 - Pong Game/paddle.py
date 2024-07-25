from turtle import Turtle

# Constants
PAD_W = 5
PAD_H = 1
HOME_R = 350
HOME_L = -350

STANDARD_MOVE = 20


class Paddle(Turtle):
    """
    Creation of a paddle object. Each game will include two paddle objects (one on left and
    one on right). Paddle objects can move up or down (the key bindings for left and right are
    exclusive to that player position [left paddle uses "W" and "S", right player uses "Up"
    and "down" arrows].

     This class has built-in methods for the following:
    - Moving the paddle object up and down.
    """
    def __init__(self, position: str):
        # Set's up a paddle object that is based on a Turtle()
        super().__init__()

        # Position data:
        if position == "right":
            self.x_position = HOME_R
        else:
            self.x_position = HOME_L
        self.y_position = 0

        # Aesthetics: Each paddle is white and 20 x 100p in size.
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PAD_W, stretch_len=PAD_H, outline=None)
        self.penup()

        # Placement.
        self.goto(self.x_position, self.y_position)

    def up(self):
        """
        Defines the ability for the paddle object to move in a positive y coordinate.
        """
        if self.ycor() < 250:
            new_y = self.ycor() + STANDARD_MOVE
            self.goto(self.xcor(), new_y)

    def down(self):
        """
        Defines the ability for the paddle object to move in a negative y coordinate.
        """
        if self.ycor() > -240:
            new_y = self.ycor() - STANDARD_MOVE
            self.goto(self.xcor(), new_y)
