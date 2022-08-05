from turtle import Screen, Turtle
from ship import Ship
from bullet import Bullet

def left():
    ship.move_left()
    bullet.move_left()

def right():
    ship.move_right()
    bullet.move_right()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)
screen.listen()


ship = Ship()
x,y = ship.pos()
# ship.penup()
# ship.goto(0,-260)
# ship.create_ship(0,-200)
# # ship.setheading(90)

bullet = Bullet()
bullet.goto(x-20,y+60)
bullet.stamp()

while True:
    screen.update()
    screen.onkeypress(left, "Left")
    # screen.onkeypress(bullet.move_left, "Left")
    screen.onkeypress(right, "Right")
    # screen.onkeypress(bullet.move_right, "Right")
    screen.onkeypress(bullet.shot, "space")
    if bullet.move:
        bullet.bullet_shot()






screen.exitonclick()