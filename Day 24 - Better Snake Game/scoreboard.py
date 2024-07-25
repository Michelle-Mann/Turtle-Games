# Name: Michelle Mann
# Project Name: Turtle Snake Game - Scoreboard
# Date: 8/28/2023
# Description: 100 Days of Code (Day 18-22) by: The App Brewery.
# Code below details how the scoreboard object will work.

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    """
    Defines a Scoreboard object. Scoreboard objects list both the current score and
    the current high score. The current high score can be read and written to an
    accessible .txt file.

    This class has built-in methods for the following:
    - Updates the scoreboard.
    - Resets the scoreboard.
    - Increases score.
    - Writes new high score to .txt file.
    """

    def __init__(self):
        super().__init__()

        # Stores the current score.
        self.score = 0

        # Reads the current highscore.
        with open("highscore.txt") as data:
            self.high_score = int(data.read())

        # Aesthetics.
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

        # Writes the current high score to the scoreboard.
        self.write_hs()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the current scoreboard and writes the new current and high scores to
        the screen. This is done every time the snake eats food and when the game
        resets.
        """
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        """
        Called on a reset game only! Checks if final score is higher than current
        high score and if so, writes that new score to our save-able high score
        file. If not, resets current score to 0 and resets the scoreboard.
        """
        # Checks if current score is greater than high score, if so, score is new
        # high score.
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_hs()

        # Resets new initialized score to 0.
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """
        Increases score every time snake eats food object.
        """
        self.score += 1
        self.update_scoreboard()

    def write_hs(self):
        """
        Writes the new high score to our high score save-able .txt file.
        """
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.high_score))

    # NOTE! We are replacing the below code which wrote "Game Over" one the playable
    # space upon collision with self or wall. Our new method will be reset.

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
