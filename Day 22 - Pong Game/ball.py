from turtle import Turtle


class Ball(Turtle):
    """
    Creation of a ball object. One ball object. Ball's direction will alternate on first-pass
    from (0, 0) to either left and right depending on who went last. Ball will bounce / reflect
    based on ball's connection with either a wall or paddle object.

     This class has built-in methods for the following:
    - Moving the object across the screen.
    - Reflection on the y-axis
    - Reflection on the x-axis
    - Reset-ing position.
    """

    def __init__(self):
        # Set's up a paddle object that is based on a Turtle()
        super().__init__()

        # Aesthetics: Ball object is a white 20 x 20 circle object.
        self.shape("circle")
        self.color("white")
        self.penup()

        # Movement options: Ball object moves diagonally at a speed of 0.1. Ball
        # moves faster with every paddle reflection.
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Dictates how a ball object will move. Ball's new position will take into account
        its current location plus its base movement factor.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Dictates how a ball object will move upon a bounce against a wall object. In this case,
        ball will reflect on the y-axis.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Dictates how a ball object will move upon a bounce against a paddle object. In this case,
        ball will reflect on the x-axis and will increase in speed.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Used after a player scores a point. Resets ball to (0, 0) and serves ball to scoring
        player.
        """
        self.goto(0, 0)
        self.bounce_x()
