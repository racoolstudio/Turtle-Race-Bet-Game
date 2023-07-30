# Import the necessary modules to create a turtle racing game.

from turtle import Turtle, Screen
import random
from line import Line

# Create the game screen.
my_screen = Screen()

# Color and y-coordinate lists for the turtles.
color = ['red', 'green', 'blue', 'yellow', 'pink', 'purple']
y_cor = [100, 60, 20, -20, -60, -100]
turtle_list = []


# Function to set the initial positions of the turtles.
def start_position():
    for i in range(len(color)):
        new_turtle = Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.color(color[i])
        new_turtle.goto(x=-250, y=y_cor[i])
        turtle_list.append(new_turtle)


# Function to check if a turtle has won the race.
def win(turtle):
    if turtle.pos()[0] >= 200:
        return True
    else:
        return False


# Function to simulate the race and determine the winner.
def race():
    winner = ''
    Over = False
    while not Over:
        for turtles in turtle_list:
            if win(turtles):
                Over = True
                winner = turtles.pencolor()
            turtles.fd(random.randint(0, 10))

    return winner


def show_message(message):
    # Create a turtle to display the message
    message_turtle = Turtle()
    message_turtle.penup()
    message_turtle.hideturtle()
    message_turtle.goto(0, 0)
    message_turtle.color('white')
    message_turtle.write(message, align='center', font=('Arial', 20, 'normal'))


# Function to execute the main game logic.
def main():
    endLine = Line(200, 150, 'white', 'green')
    startLine = Line(-230, 150, 'yellow', 'red')


    my_screen.setup(width=500, height=400)
    my_screen.title('Turtle Race Bet')

    # Get user input for the turtle they think will win the race.
    user_input = my_screen.textinput(title='Make Your Bet 🥷',
                                     prompt='Which turtle would win the race ? 🤷 Enter a color: red,green,blue,'
                                            'yellow,pink, or purple ').lower()
    start_position()

    my_screen.bgcolor('black')
    endLine.draw()
    startLine.draw()
    # Start the race and determine the winner.
    won = race()

    if won == user_input:
        show_message(f'{won.upper()} won the race !!! 🥇\nYou won the bet !!! 🏆')

    else:
        show_message(f'{won.upper()} won the race !!! 🥇\nYou Loss the bet🫣 !!!')


main()
my_screen.exitonclick()
