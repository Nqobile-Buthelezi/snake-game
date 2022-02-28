from turtle import Turtle

FONT_SIZE = 15
FONT = ("Arial", FONT_SIZE, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.plus_one()

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=True, align="center", font=FONT)

    def plus_one(self):
        self.score += 1
        self.setposition(x=0, y=270)
        self.clear()
        self.write(arg=f"Score: {self.score}", move=True, align="center", font=FONT)

