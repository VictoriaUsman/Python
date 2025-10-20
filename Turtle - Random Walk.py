import turtle
from turtle import Turtle, Screen
import random

PongPagong = Turtle()
Pong_Salamin = Screen()
turtle.colormode(255)
PongPagong.shape("turtle")
PongPagong.pensize(12)
PongPagong.speed(5)

direction = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for dance in range(500):
    PongPagong.color(random_color())
    PongPagong.forward(40)
    PongPagong.setheading(random.choice(direction))



Pong_Salamin.exitonclick()