import pgzrun
import random
WIDTH=300
HEIGHT=300
def draw():
    x=0
    y=100
    w=300
    h=100
    o=1
    rad=150
    screen.fill("black")
    while o==1:
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        re=Rect((x,y),(w,h))
        screen.draw.rect(re,(r,g,b))
        screen.draw.circle((150,150),(rad),(r,g,b))
        rad=rad-5
        x=x+5
        y=y-5
        w=w-10
        h=h+10
        if x==105:
            o=2
    screen.draw.text("Pattern",center=(150,150),color=(r,g,b))
pgzrun.go()