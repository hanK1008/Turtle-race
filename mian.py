from turtle import Screen,Turtle
import random

screen = Screen()                      # making of screen to draw
screen.setup(width=500, height=400)    # Size of screen to show

# for making the popup for the user input screen.textinput
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the racce input color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
turtles = []


for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()                            # Turtle is get measure from the middle of the size of the turtle
    t.goto(x=-230, y=y_position[i])     # AS turtle default size is 40*40 pixle  middle = 20>>> 250-20 = 230
    turtles.append(t)


# For running the game
game_on = False

if user_input:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            game_on = False
            if user_input == turtle.pencolor():
                print(f"You've won. {turtle.pencolor()} is the winner.")
            else:
                print(f"You've lose. {turtle.pencolor()} is the winner.")

        random_movemnt = random.randint(0, 10)
        turtle.forward(random_movemnt)


screen.exitonclick()
