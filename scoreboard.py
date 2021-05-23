FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.current_level = 0
        self.write(f"Level: {self.current_level}", False, "left", FONT)

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", False, "left", FONT)
        print(f"leve_up {self.current_level}")

    def finish_game(self):
        self.current_level += 1
        self.home()
        self.write("GAME OVER", False, "center", FONT)
