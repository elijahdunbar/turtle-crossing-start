import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Spawning the player and add controls
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

#Spawn cars and make them move
counter = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Move every created car
    cars.move()
    #Detect player collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()




    #Create a new car every 6th loop
    if counter % 6 == 0:
        cars.create_car()

    #Detect if player reached other end
    if player.at_end():
        player.to_begining()
        cars.increase_speed()
        scoreboard.next_level()

    #Increment to keep track of when to spawn a car
    counter += 1






screen.exitonclick()