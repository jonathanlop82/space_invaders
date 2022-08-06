from turtle import Turtle
import bullet     


class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("green")
        self.create_ship(0,-200)


    def create_ship(self,x=0,y=-200):
        self.goto(0,-200)
        for j in range(1,4):
            for i in range(j):
                self.goto(x  + (i * 20 - j*10) ,y + (j * -20) )
                self.stamp()

    def move_left(self):
        x,y = self.pos()
        if x > -240:
            self.clear()
            self.create_ship(x- 20 -20, -200)

    def move_right(self):
        x,y = self.pos()
        if x < 260:
            self.clear()
            self.create_ship(x + 20, -200)


