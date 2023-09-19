from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(x=300, y=random.randint(-250, 250))
        self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.goto(x=car.xcor() - self.car_speed, y=car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT