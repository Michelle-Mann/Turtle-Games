from turtle import Turtle

# Constants.
FONT_SCORE = ("Courier", 80, "normal")
FONT_GO = ("Courier", 16, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    """
    Creation of a scoreboard object. Scoreboard object keeps score for both the left and right
    player simultaneously. Each time a player misses the ball with the paddle, the opposing
    player will score a point. Scoreboard class is also responsible for displaying "Game
    Over" content.

     This class has built-in methods for the following:
    - Update the scoreboard
    - Updates points for Left player
    - Updates points for Right player
    - Process for game over.
    """

    def __init__(self):
        super().__init__()
        # Aesthetics: Text is white.
        self.color("white")
        self.penup()
        self.hideturtle()

        # Stores the scores for both left and right player. Writes these to screen.
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Defines behavior for the scoreboard itself. Including when to clear the console
        and update with new scores.
        """
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align=ALIGN, font=FONT_SCORE)
        self.goto(100, 180)
        self.write(self.r_score, align=ALIGN, font=FONT_SCORE)

    def l_point(self):
        """
        Adds a point to the left player and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Adds a point to the right player and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Protocol for game over scenario.
        """
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGN, font=FONT_GO)
        self.goto(0, 20)
        winner = None

        if self.l_score > self.r_score:
            winner = "Left"
        else:
            winner = "Right"
        self.write(f"{winner} Player Wins!", align=ALIGN, font=FONT_GO)
