import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle do you think will win the race? Enter a color: " ).lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
racing_turtles = []

# loop for creating six different turtles
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    racing_turtles.append(new_turtle)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in racing_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrats! You picked the winning turtle, {winning_color}!")
                print(f" Fame and riches are coming your way. Your life will change as your destiny is now bound to this {winning_color} turtle...")
            else:
                print(f"You've lost :( The {winning_color} turtle is the winner. Better luck next time!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





# start listening for events


screen.exitonclick()
