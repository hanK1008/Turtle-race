from turtle import Screen,Turtle
import random

screen = Screen()                      # making of screen to draw
screen.setup(width=500, height=400)    # Size of screen to show.
money = 500
width = screen.window_width()
names = []
# players = ["Sahil", "Swapnil", "sahil", "PAL", "hanK", "stiven"]

number_of_players = screen.numinput(title="Number of players",
                                    prompt="Please enter the number of players will play the game")

# for making the popup for the user input screen.textinput
for i in range(6):
    user_name = screen.textinput(title="Enter your name", prompt="Please Enter you name below")
    # if you want to insert players name manually then use above line and
    # remove (comment out) players list and below code change player[i] to user_name

    user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race guess color")
    user_bet = screen.numinput(title= "Enter your bet amount", prompt=f"How much money do you want to bet. "
                                                                      f"You have ${money}")
    player = {"name": user_name, "color": user_input, "bet": user_bet, "money": 500}
    names.append(player)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
turtles = []
x_position = (width/2)-20

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()                            # Turtle is get measure from the middle of the size of the turtle
    t.goto(x=-x_position, y=y_position[i])     # AS turtle default size is 40*40 pixle  middle = 20>>> 250-20 = 230
    turtles.append(t)


# For running the game
game_on = True

# while game_on:
#     for turtle in turtles:
#         if turtle.xcor() >= 230:
#             game_on = False
#             if names.values() == turtle.pencolor():
#                 money += (names["user_bet"]*5)
#                 print(f"{names.keys()} won. {turtle.pencolor()} is the winner.\nYou have ${money} left")
#             else:
#                 money -= names["user_bet"]
#                 print(f"{names.keys()} lose. {turtle.pencolor()} is the winner.\nYou have ${money} left")
#
#         random_movement = random.randint(0, 10)
#         turtle.forward(random_movement)


while game_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            game_on = False
            for user in names:
                if user["color"] == turtle.pencolor():
                    user["money"] += user["bet"]*3
                    print(f"{user['name']} is the winner ")
                else:
                    user["money"] -= user["bet"]

        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)

# print(names)
print("Name      Money")
for i in names:
    print(f"{i['name']}     ${i['money']} ")
screen.exitonclick()
