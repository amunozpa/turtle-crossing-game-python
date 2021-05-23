STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.speed(0)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.lastline = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        """Sirve para definir que hará cuando alcance la coordenada asignada"""
        self.goto(STARTING_POSITION)
