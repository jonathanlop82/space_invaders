from turtle import Turtle  


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.move = False

    def shot(self):
        self.move = True


    def bullet_shot(self):
        x,y = self.pos()
        self.clear()
        self.goto(x,y+5)

    def move_left(self):
        x,y = self.pos()
        if x > -260:
            self.clear()
            self.goto(x-30,y)

    def move_right(self):
        x,y = self.pos()
        if x < 240:
            self.clear()
            self.goto(x+30,y)



