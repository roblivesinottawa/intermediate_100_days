from turtle import Turtle, Screen
import turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")


for _ in range(10):
    timmy.forward(100)
    timmy.left(90)


screen = Screen()
screen.exitonclick()
