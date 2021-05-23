COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.speed(0)
        self.shape("square")
        self.shapesize(1, 2)
        self.position()
        self.cord_x = STARTING_MOVE_DISTANCE
        self.move()

    def position(self):
        self.goto(random.randrange(280, 3000, 1), random.randint(-200, 200))

    def move(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - self.cord_x)
        else:
            self.position()

    def stop(self):
        self.cord_x = 0

    def increment_move(self):
        self.cord_x += MOVE_INCREMENT
