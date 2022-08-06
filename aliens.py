from turtle import Turtle


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('alien.gif')


    def move(self):
        x,y = self.pos()
        self.clear()
        self.goto(x + 40, y)
