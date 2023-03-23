def drzewo_binarne(z, stopien, dl_bok):
    if stopien == 0:
        pozycja = z.pos()
        z.forward(dl_bok)
        z.goto(pozycja)
    else:
        pozycja = z.pos()
        z.forward(dl_bok)
        z.left(45)
        drzewo_binarne(z, stopien-1, dl_bok/2)
        z.right(90)
        drzewo_binarne(z, stopien-1, dl_bok/2)
        z.left(45)
        z.goto(pozycja)

from turtle import Turtle
zlw = Turtle()

zlw.penup()
zlw.goto(-20,-20)
zlw.pendown()
zlw.left(90)

drzewo_binarne(zlw, 3, 50)