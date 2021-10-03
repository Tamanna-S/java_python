from turtle import Turtle

class Score(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.color("chartreuse")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align = "center", font = ("courier", 20," normal") )

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("..Game Over.." , align="center", font= ("courier", 20," normal") )
