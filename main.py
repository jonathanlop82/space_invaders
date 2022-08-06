from turtle import Screen, Turtle
from ship import Ship
from bullet import Bullet
from aliens import Aliens

def left():
    ship.move_left()
    if not bullet.move:
        bullet.move_left()

def right():
    ship.move_right()
    if not bullet.move:
        bullet.move_right()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)
screen.listen()
screen.addshape('alien.gif')


ship = Ship()
x,y = ship.pos()


bullet = Bullet()
bullet.goto(x-20,y+60)
bullet.stamp()

aliens = []
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(Aliens())
        temp[j].penup()
        temp[j].goto(-240 +(i * 110) , 240 - (j * 60))
        temp[j].stamp()
    aliens.append(temp)
    
    

while True:
    screen.update()
    screen.onkeypress(left, "Left")
    # screen.onkeypress(bullet.move_left, "Left")
    screen.onkeypress(right, "Right")
    # screen.onkeypress(bullet.move_right, "Right")
    screen.onkeypress(bullet.shot, "space")
    if bullet.move:
        bullet.bullet_shot()

    bullet_x, bullet_y = bullet.pos()
    if bullet_y > 310:
        bullet.clear()
        x,y = ship.pos()
        bullet.move = True
        bullet = Bullet()
        bullet.goto(x-20,y+60)
        bullet.stamp()

    for i in range(4):
        for j in range(4):
            aliens[i][j].move()







screen.exitonclick()