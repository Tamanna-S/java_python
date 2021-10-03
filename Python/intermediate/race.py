from turtle import Turtle, Screen, color, speed, textinput, title, xcor
import random

y_pos = [-100,-60,-20,20,60,100]

all_turtules=[]
colors = ["orange","red","green","blue","yellow","purple"]

def raceSpeed():
    rand_speed = random.randint(0,10)
    return rand_speed
race_over= True

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 500)

for _ in range(6):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.goto(-280,y_pos[_])
    turtle.color(colors[_])
    all_turtules.append(turtle)

user = textinput(title = "what do u think?" , prompt = "which turtle will win this game..? enter his color: ").lower()

if user:
    race_over = False

while not race_over:
    for tur in all_turtules:
        tur.forward(raceSpeed())
        if tur.xcor() >=273:
            win_color = tur.pencolor()
            race_over = True
            break

if win_color == user:
    print("\n")
    print(f"you win! the winner is the {win_color} turtle..\n")
else:
    print("\n")
    print(f"oops, you lose! you've think of {user} turtle but, the winner is the {win_color} turtle..\n")
        