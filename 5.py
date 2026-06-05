import tkinter
from PIL import ImageTk, Image
import random

pocet = int(input("Pocet minci: "))



def random_coordinate_x():
    valid_x = list(range(1, 186)) + list(range(314, 500))
    x = random.choice(valid_x)
    return x

def random_coordinate_y():
    valid_y = list(range(64, 250))
    y = random.choice(valid_y)
    return y


root = tkinter.Tk()
root.geometry("500x500")

canvas = tkinter.Canvas(root,bg="white", height=500, width=500)

mesec = ImageTk.PhotoImage(Image.open("mesec.png"))
canvas.create_image(250,250,anchor="center", image=mesec)

minca = ImageTk.PhotoImage(Image.open("minca.png"))
for i in range(pocet):
    canvas.create_image(random_coordinate_x(), random_coordinate_y(),anchor="center", image=minca)

canvas.pack()


root.mainloop()