import turtle
from turtle import Turtle, Screen
import pandas
import timeit


Game = Turtle()
Screen = Screen()

Screen.title("Welcome to U.S. States Game")
background = "blank_states_img.gif"
Screen.addshape(background)
Game.shape(background)

Game_On = True
data = pandas.read_csv("50_states.csv")
score = 0
while Game_On:
    hula = turtle.textinput(f"U.S States Game: {score}/50" , "Guess the 50 States")
    for i in data.state:
        x = float(data.x[data.state == i])
        y = float(data.y[data.state == i])
        if i == hula:
            hula = turtle
            hula.hideturtle()
            hula.penup()
            hula.speed(5)
            hula.goto(x=x, y=y)
            hula.write(i, align="center", font=("Arial", 13, "bold"))
            score += 1
            if score => 50:
                Game_On = False




Screen.exitonclick()