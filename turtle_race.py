from turtle import Turtle, Screen
import random as rd

# Set starting positions for turtles
def goto_start_pos(turtle_list):
    x = -280
    y = 150
    for tim in turtle_list:
        tim.goto(x, y)
        y -= 60

# Draw the racetrack (start and finish lines) and display a welcome message
def race_setup():
    tim = Turtle()
    tim.speed = 'fastest'
    tim.hideturtle()

    # Finish line
    tim.penup()
    tim.goto(295, -250)
    tim.down()
    tim.goto(295, 250)

    # Starting line
    tim.penup()
    tim.goto(-260, -250)
    tim.down()
    tim.goto(-260, 250)

    # Welcome message
    tim.penup()
    tim.goto(0, 220)
    tim.write("Welcome to the Turtle Race!", align="center", font=("Arial", 18, "bold"))

# Display winner announcement
def winner_notice(msg):
    tim = Turtle()
    tim.penup()
    tim.goto(0, -250)
    tim.write(arg=msg, align="center", font=("Arial", 16, "bold"))
    tim.hideturtle()

# Initialize game
is_game_on = False
screen = Screen()
screen.setup(width=650, height=550)
race_setup()

# Create turtles
color_list = ['red', 'green', 'blue', 'yellow', 'violet', 'orange']
turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.speed('slow')
    new_turtle.color(color_list[i])
    turtles.append(new_turtle)

goto_start_pos(turtles)

# Prompt user for a bet
user_color = screen.textinput(title='Make your bet!', prompt='Which turtle will win the race? Enter a color: ')
if user_color:
    is_game_on = True

# Start the race
while is_game_on:
    for turtle in turtles:
        turtle.forward(rd.randint(1, 10))  # Random movement
        if turtle.xcor() > 280:
            is_game_on = False
            winning_color = turtle.pencolor()

            # Display race results in the console and screen
            if winning_color == user_color:
                message=f"You've Won! {winning_color.capitalize()} turtle wins!"
                print(message)
                winner_notice(message)
            else:
                message=f"You've Lost! {winning_color.capitalize()} turtle wins!"
                print(message)
                winner_notice(message)

screen.exitonclick()
