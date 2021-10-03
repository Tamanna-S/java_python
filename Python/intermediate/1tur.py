import turtle
tur = turtle.Turtle()
tur.shape("turtle")
turtle.colormode(255)
tur.color(0,255,0)
tur.pensize(7)

screen = turtle.Screen()
screen.bgcolor("black")


for move in range(4):
    tur.forward(100)
    tur.right(90)








screen.exitonclick()