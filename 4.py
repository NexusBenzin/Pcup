from turtle import *

def kniha(sirka,vyska):
    for i in range(2):
        fd(sirka)
        lt(90)
        fd(vyska)
        lt(90)

def polica(sirka, vyska):


    penup()
    fd(10)
    pendown()

    for i in range(10):
        kniha(sirka,vyska)
        penup()
        fd(sirka + 10)
        pendown()



    fd(10)
    bk(sirka * 10 + 10 * 10 + 30)

speed(0)
polica(30, 100)
hideturtle()

exitonclick()
