from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    """
    Creation of a scoreboard. Our scoreboard will track what level our player is currently on
    and will let the player know when they've completed that level!

     This class has built-in methods for the following:
    - Updating the scoreboard
    - Announcing a new level
    - Announcing game over.
    """

    def __init__(self):
        super().__init__()
        # Aesthetics: Font is white.
        self.color("white")
        self.penup()
        self.hideturtle()

        # Stores our current level (default: 1) and displays on scoreboard.
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Displays our current level on the upper left hand corner of our screen.
        """
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def new_level(self):
        """
        Increments our current level when a level has been complete. And displays a completion
        notice to the user.
        """
        self.level += 1
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"Level: {self.level - 1} - COMPLETE!", align="center", font=FONT)

    def game_over(self):
        """
        Displays "Game Over" when a collision between the player and a car object has
        happened.
        """
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
