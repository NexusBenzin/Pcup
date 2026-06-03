from turtle import *

def square():
    for i in range(4):
        fd(100)
        lt(90)

def move_square(side: str = "right"):
    square()
    if side == "right":
        forward(10)
    elif side == "left":
        backward(10)
    clear()



setup(500, 500)
speed(0)
while True:
    x, y = position()
    print(x)
    if x >= 150:
        for i in range(45):
            move_square("left")
    elif x <= -150:
        for i in range(45):
            move_square("right")
    else:
        move_square("right")

