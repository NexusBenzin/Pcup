from turtle import *

def kresli(pocet, dlzka, hrubka, farba):
    pensize(hrubka)
    color(farba)
    angle = 360 / pocet
    for i in range(pocet):
        forward(dlzka)
        backward(dlzka)
        left(angle)

    penup()
    home()
    backward(dlzka / 2)
    right(90)
    forward(dlzka)
    left(90)
    forward(dlzka / 2)
    pensize(1)
    color("yellow")
    pendown()
    begin_fill()
    circle(dlzka)
    end_fill()



# kresli(6,30,50,'red')
# kresli(25,100,2,'yellow')
exitonclick()
