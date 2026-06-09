from turtle import *
import random


def metla(rucka, pocet, dlzka):
    angle = 180 / pocet


    fd(rucka)
    left(90)
    forward(dlzka)
    backward(dlzka)
    for i in range(pocet):
        right(angle)
        forward(dlzka)
        backward(dlzka)
    left(90)
    backward(rucka)

def metly():
    smery = [0, 90, 180, 270]

    pocet = random.randint(1, 10)
    smer = random.choice(smery)
    left(smer)
    for i in range(pocet):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        penup()
        goto(x, y)
        pendown()
        metla(100, 7, 20)



screensize(500,500)
metly()
exitonclick()


