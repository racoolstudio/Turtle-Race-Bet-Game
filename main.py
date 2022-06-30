from turtle import Turtle, Screen
import random

my_screen = Screen()
# def move_forward():
#     t.forward(10)
#
#
# def move_back():
#     t.back(10)
#
#
# def counter_clock():
#     t.left(10)
#
#
# def clock_wise():
#     t.right(10)
#
#
# def pen_up():
#     t.penup()
#
#
# def pen_down():
#     t.pendown()
#
#
# def clear():
#
#     t.clear()
#     t.penup()
#     t.home()

color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y_cor = [100, 60, 20, -20, -60, -100]
turtle_list = []


def start_position():
    for i in range(len(color)):
        new_turtle = Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.color(color[i])
        new_turtle.goto(x=-250, y=y_cor[i])
        turtle_list.append(new_turtle)


def win(turtle):
    if turtle.pos()[0] >= 200:
        return True
    else:
        return False


def race():
    winner = ''
    isover = False
    while not isover:
        for turtles in turtle_list:
            if win(turtles):
                isover = True
                winner = turtles.pencolor()
            turtles.fd(random.randint(0, 10))

    return winner


def main():
    line = Turtle()
    line.hideturtle()
    my_screen.setup(width=500, height=400)
    my_screen.title('Turtle Race')
    bandw = ['yellow', 'white']

    user_input = my_screen.textinput(title='Make Your Bet 🥷',
                                     prompt='Which turtle would win the race ? 🤷 Enter a color: ').lower()
    start_position()

    my_screen.bgcolor('black')
    line.penup()

    line.goto(200, 150)
    line.right(90)
    line.width(10)
    for i in range(10):
        line.pendown()
        if i % 2 == 0:
            line.color(bandw[0])
        else:
            line.color(bandw[1])
        line.fd(30)

    won = race()
    #
    print(f'{won.upper()} won the race !!! 🥇')
    if won == user_input:
        print('You won the best !!! 🏆')
    else:
        print('You Loss🫣 !!!')


main()

# my_screen.listen()
# my_screen.onkey(key='w', fun=move_forward)
# my_screen.onkey(key='s', fun=move_back)
# my_screen.onkey(key='a', fun=counter_clock)
# my_screen.onkey(key='d', fun=clock_wise)
# my_screen.onkey(key='u', fun=pen_up)
# my_screen.onkey(key='f', fun=pen_down)
# my_screen.onkey(key='c', fun=clear)
my_screen.exitonclick()
