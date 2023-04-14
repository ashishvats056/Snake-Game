from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self. speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.choice(range(-280, 281, 20))
        random_y = random.choice(range(-280, 281, 20))
        self.setposition(random_x, random_y)
