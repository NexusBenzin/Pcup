from turtle import *

def kniha(sirka,vyska):
    for i in range(2):
        fd(sirka)
        lt(90)
        fd(vyska)
        lt(90)

def polica(sirka, vyska):
    lt(90)
    fd(vyska)
    bk(vyska)
    rt(90)

    penup()
    fd(10)
    pendown()

    for i in range(10):
        kniha(sirka,vyska)
        penup()
        fd(sirka + 10)
        pendown()


    lt(90)
    fd(vyska)
    bk(vyska)
    rt(90)


polica(30, 100)
exitonclick()