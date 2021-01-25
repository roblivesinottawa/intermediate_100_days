from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["red", "green", "orange", "blue", "yellow"]

def draw(n_sides):
    angle = 360 / n_sides
    for shape in range(n_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw(shape_side)

screen = Screen()
screen.exitonclick()