from turtle import Turtle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
path = BASE_DIR / "data.txt"

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # Read high score
        with open(path) as data:
            self.highscore = int(data.read())

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT
        )

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(path, mode="w") as data:
                data.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()
