import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, 'Up')

pool_car = []
for c in range(30):
    car = CarManager()
    pool_car.append(car)

score = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.09)
    for car in pool_car:
        # Detect colision with cars
        car.move()
        if player.distance(car) < 30 and car.towards(player) >= 180:
            score.finish_game()
            car.stop()
            game_is_on = False
            pass
        else:
            if player.ycor() > player.lastline:
                player.reset()
                score.level_up()
                for c in pool_car:
                    c.increment_move()

    screen.update()

screen.exitonclick()
