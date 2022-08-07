from turtle import Turtle


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('alien.gif')
        self.penup()

    def move_left(self):
        x,y = self.pos()
        self.goto(x-3,y)

    def move_right(self):
        x,y = self.pos()
        self.goto(x+3,y)

    def move_down(self):
        x,y = self.pos()
        self.goto(x,y-20)

