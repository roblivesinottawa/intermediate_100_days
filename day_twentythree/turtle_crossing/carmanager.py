from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# create a class and methods to manage the movement of the cars
class CarManager:
    def __init__(self):
 # create a variable to store all cars and set it to an empty list
        self.all_cars = []
# create a varaible that will set the starting speed of the cars
        self.car_speed = STARTING_MOVE_DISTANCE

# this method will create cars along the y line
# and set the properties for the cars
    def create_car(self):
        # create less cars
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # this will stretch the turtle
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # define where it's going to go on the screen
            yrandom = random.randint(-250, 250)
            # cars will go to the very edge of the screen
            new_car.goto(300, yrandom)
            # then it will be added to the list of all cars
            self.all_cars.append(new_car)



    # create a new method to move all cars
    def move_cars(self):
        # FOR EACH OF THE CARS IN THE LIST
        for car in self.all_cars:
            # each car will be moved by the distance stored in the variable
            car.backward(self.car_speed)
    
    # create a method that will increase the speed of the cars by 10 once at the end line
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
