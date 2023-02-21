
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title= "Make a bet.", prompt="Which turtle will win the race. Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-235, y= y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        i.forward(random_distance)

screen.exitonclick()