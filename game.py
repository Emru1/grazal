from player import *

screenSize(800, 600)
playsprite = newSprite("szkielet/preview.png")

//test

xspeed = 10
yspeed = 0
a = Player(playsprite)
colour = parseColour('black')
setBackgroundColour(colour)
a.show()
x = 400
y = 300
a.move(x, y)
tick(60)
while True:
    if True:
        if keyPressed("up"):
            yspeed -= 1
        elif keyPressed("down"):
            yspeed += 1
        elif keyPressed("left"):
            xspeed -= 1
        elif keyPressed('right'):
            xspeed += 1

    if xspeed > 300:
        xspeed = 300
    if xspeed < -300:
        xspeed = -300
    if yspeed > 300:
        yspeed = 300
    if yspeed < -300:
        yspeed = -300
    x += xspeed/1000
    if x > 900:
        x = -100
    if x < -100:
        x = 900
    y += yspeed/1000
    if y > 700:
        y = -100
    if y < -100:
        y = 700
    a.move(x, y)
    if xspeed != 0:
        if xspeed > 0:
            xspeed -= 0.5
        else:
            xspeed += 0.5

    if yspeed != 0:
        if yspeed > 0:
            yspeed -= 0.5
        else:
            yspeed += 0.5
