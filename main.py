from turtle import Turtle, Screen
import random

# Creating a turtle object
tur = Turtle()
tur.speed("fastest")


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tur.color(R, G, B)


# Draw a circle
step = 0
while step <= 360:
    change_color()
    tur.circle(100)
    tur.setheading(step)
    step += 10

screen = Screen()
screen.exitonclick()
