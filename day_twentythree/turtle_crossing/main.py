# import the turtle and screen module from the turtle library
from turtle import Screen, Turtle
# import the time module which times the application at run time
import time
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

# instantiate the screen module by creating a screen variable
screen = Screen()
# set the size of the screen
screen.setup(width=600, height=600)
# this method turns off animation
screen.tracer(0)

# instantiate the Player class
player = Player()
# instantiate the CarManager class
car_manager = CarManager()
# instantiate the Scoreboard class
scoreboard = Scoreboard()

# get the program to listen to keyboard 
screen.listen()
screen.onkey(player.move_up, "Up")



# variable to initialize the loop by setting it to True
game_on = True

# start the loop 
while game_on:
    # this method times actions in the application at run time
    time.sleep(0.1)
    # this method cancels out the tracer method when called
    screen.update()
# this will create a new car every 0.1 seconds
    car_manager.create_car()
# get all the cars to move by 5 paces
    car_manager.move_cars()


    # detect collision with cars
    # the loop will get ahold of all the cars
    for car in car_manager.all_cars:
        # check is the distance is less than 20px because that is the size of the cars
        if car.distance(player) < 20:
            # if that is true, then game will stop
            game_on = False
            scoreboard.game_over()

    # detect successful crossing
    # call the method created at Player class
    if player.end_line():
        # this takes the turtle back to the starting line
        player.go_to_start()
        # this will level up the score
        car_manager.level_up()
        # update the scoreboard
        scoreboard.increase_level()


   

  





# this method is initialized when screen is clicked
screen.exitonclick()