import pgzrun
WIDTH=500
HEIGHT=300
def draw():
    screen.fill("purple")
    r=Rect((50,50),(150,100))
    screen.draw.rect(r,"orange")
    r2=Rect((350,50),(100,150))
    screen.draw.filled_rect(r2,"orange")
pgzrun.go()