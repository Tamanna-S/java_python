from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME..")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

playing = True

while playing:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_left, "Left")

    if snake.head.distance(food) < 15:
        food.rand_pos()
        score.increase_score()
        snake.extend_snake()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        playing = False

screen.exitonclick()