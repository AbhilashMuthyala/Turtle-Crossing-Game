from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# random car generation

class CarManager:
    def __init__(self):
        self.car_list = []
        self.level = 1
        self.rand = 10

    def create_car(self):
        car = Turtle()
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.penup()
        car.sety(0)
        car.setx(280)
        car.fillcolor(random.choice(COLORS))
        car.setx(280)
        i = random.randint(-280,280)
        car.sety(i)
        self.car_list.append(car)

    def move_car(self,player):
        for car in self.car_list:
            car.setx(car.xcor()-MOVE_INCREMENT)
            if player.distance(car) < 25:
                return True
            if car.xcor() < -280:
                car.hideturtle()
                self.car_list.remove(car)





