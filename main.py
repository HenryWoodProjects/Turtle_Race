from turtle import Turtle, Screen
import random

pen = Turtle(shape="arrow")
pen.hideturtle()
pen.speed(0)

colours = ["blue", "green", "red", "yellow", "orange", "purple"]
y_positions = [150, 90, 30, -30, -90, -150]
all_turtles = []


def draw_line(start_x, start_y, end_x, end_y):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.goto(end_x, end_y)
    pen.penup()


is_race_on = False
screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

draw_line(-220, 200, -220, -200)
draw_line(220, 200, 220, -200)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.goto(-220, y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_colour = turtle.fillcolor()
            if winning_colour == user_bet.lower():
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
