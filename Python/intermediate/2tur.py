import turtle
import random
tur = turtle.Turtle()
turtle.colormode(255)
tur.shape("turtle")
tur.speed("fastest")
tur.hideturtle()

screen = turtle.Screen()
screen.bgcolor(0,0,0)

def color():
    r= random.randint(1,255)
    g= random.randint(1,255)
    b= random.randint(1,255)

    n_color = (r,g,b)
    return n_color

def circle(radius):
    for _ in range (int(360/radius)):
        tur.color(color())
        tur.circle(100)
        tur.setheading(tur.heading() + radius)

circle(3)

screen.exitonclick()