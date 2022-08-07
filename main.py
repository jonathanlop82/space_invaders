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

direction = "right"
down = False
aliens_count = 16
game_over = False

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

aliens_list = []

space = 120
height = 70

for j in range(4):
    for i in range(4):
        aliens = Aliens()
        aliens.goto(-240 + space * i,260 - height * j)
        aliens_list.append(aliens)
    

while not game_over:
    # aliens.move()
    if aliens_count == 0:
        win = Turtle()
        win.hideturtle()
        win.color('white')
        win.goto(0,0)
        win.write("YOU WIN", False, align='center', font=('Courier', 60, 'normal'))
        game_over = True
    

    screen.update()
    
    for a in aliens_list:
        x,y = a.pos()
        if x < -260:
            direction = "right"
            down = True
            
        elif x > 260:
            direction = "left"
            down = True

        if direction == "right":
            a.move_right()
        else:
            a.move_left()


    for a in aliens_list:
        if down:
            a.move_down()
    
    down = False

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
    

    for al in aliens_list:
        if al.distance(bullet) < 50:
            # x,y = al.pos()
            aliens_count -= 1
            al.goto(0,1400)
            bullet.goto(0,310)
            bullet.clear()
            x,y = ship.pos()
            bullet.move = True
            bullet = Bullet()
            bullet.goto(x-20,y+60)
            bullet.stamp()
            # sq.reset()

        alx,aly = al.pos()
        if aly < -190:
            lose = Turtle()
            lose.hideturtle()
            lose.color('white')
            lose.goto(0,0)
            lose.write("YOU LOSE", False, align='center', font=('Courier', 60, 'normal'))
            game_over = True
    
    


screen.exitonclick()