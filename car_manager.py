from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.movespeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, random.randint(-250, 250))
        self.all_cars.append(car)

    def increase_speed(self):
        self.movespeed += MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.movespeed
            car.goto(new_x, car.ycor())


