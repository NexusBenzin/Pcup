import tkinter
import random
from PIL import Image, ImageTk

chrobak_x = random.randrange(100, 400, 10)
chrobak_y = random.randrange(100, 400, 10)

root = tkinter.Tk()
root.geometry("500x500")

canvas = tkinter.Canvas(root, background="white", width=500, height=500)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("lienka.png"))
lienka = canvas.create_image(10, 450, image=img, anchor="nw")

img2 = ImageTk.PhotoImage(Image.open("chrobacik.png"))
chrobak = canvas.create_image(chrobak_x, chrobak_y, image=img2, anchor="nw")


def check():
    coords = canvas.coords(lienka)
    coords2 = canvas.coords(chrobak)
    print(coords)
    print(coords2)
    if coords == coords2:
        print("Ahoj")


def arrow_up(event):
    canvas.move(lienka, 0, -10)
    check()

def arrow_down(event):
    canvas.move(lienka, 0, 10)
    check()

def arrow_left(event):
    canvas.move(lienka, -10, 0)
    check()

def arrow_right(event):
    canvas.move(lienka, 10, 0)
    check()


canvas.bind_all("<Up>", arrow_up)
canvas.bind_all("<Down>", arrow_down)
canvas.bind_all("<Left>", arrow_left)
canvas.bind_all("<Right>", arrow_right)



root.mainloop()


