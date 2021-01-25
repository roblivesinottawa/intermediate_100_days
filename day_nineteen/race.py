from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make a bet", prompt="who will win the race? enter a color: ")
colors = ["red", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20]
all_turtles = []

for turtle_index in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


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