import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
car_manager = CarManager()
board = Scoreboard()
game_is_on = True
loop = 1
level = 1
while game_is_on:
    time.sleep(0.1*level)
    screen.update()
    player.move()
    if loop%6 == 0:
        car_manager.create_car()
    loop += 1
    out = car_manager.move_car(player)
    if out:
        board.gameover()
        game_is_on = False
    if player.ycor() > 280:
        level += 1
        board.board_refresh(level)
        player.reset()

    screen.update()

screen.exitonclick()
