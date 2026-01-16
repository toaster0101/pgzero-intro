import pgzrun
WIDTH=300
HEIGHT=300
def draw():
    o=1
    WhiteOrRed=1
    rad=100
    screen.fill("blue")
    color="white"
    while o==1:
        screen.draw.filled_circle((150,150),(rad),(color))
        if WhiteOrRed%2==0:
            color="white"
        else:
            color="red"
        WhiteOrRed=WhiteOrRed+1
        rad=rad-10
        if rad==0:
            o=2
pgzrun.go()