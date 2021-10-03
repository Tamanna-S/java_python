from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.xy_position = [ (-20,0) , (0,0) , (20,0) ]
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in self.xy_position:

            self.add_sqr(position)
            
    def add_sqr(self, position):
        sqr = Turtle("square")
        sqr.penup()
        sqr.color("chartreuse")
        sqr.goto(position)
        self.snake.append(sqr)

    def extend_snake(self):
        self.add_sqr(self.snake[-1].position())
    

    def move(self):
        for move in range (len (self.snake)-1, 0, -1):
            new_x = self.snake[move-1].xcor()
            new_y = self.snake[move-1].ycor()
            self.snake[move].goto(new_x, new_y)
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

