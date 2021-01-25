from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput("make a bet", "who will win the race? enter a color: ")
colors = ["red", "blue", "purple", "green"]

tom = Turtle(shape="turtle")
tom.color(colors[0])
tom.penup()
tom.goto(x=270, y=-150)

tim = Turtle(shape="turtle")
tim.color(colors[1])
tim.penup()
tim.goto(x=270, y=-120)

timmy = Turtle(shape="turtle")
timmy.color(colors[2])
timmy.penup()
timmy.goto(x=270, y=-90)

tommy = Turtle(shape="turtle")
tommy.color(colors[3])
tommy.penup()
tommy.goto(x=270, y=-60)

all_turtles = [tom, tim, timmy, tommy]

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is the winner.")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner.")
        
        
        
        distance = random.randint(0, 10)
        turtle.forward(distance)







screen.exitonclick()