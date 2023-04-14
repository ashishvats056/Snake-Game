# Snake Game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
game_on = True


def finish_game():
    global game_on
    game_on = False


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("The Famous Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=finish_game, key="space")

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 1:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_score()
            for part in snake.segments:
                screen.update()
                time.sleep(0.1)
                snake.move()
            snake.reset_snake()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_score()
                for part in snake.segments:
                    screen.update()
                    time.sleep(0.1)
                    snake.move()
                snake.reset_snake()

    screen.exitonclick()
