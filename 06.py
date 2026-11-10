import tkinter
from PIL import Image, ImageTk
import random



def move_ball():
    y = random.randint(-150, 150)
    canvas.move(lopta, 350, y)


    list = []
    for i in range(-22, 22):
        list.append(i)

    print(y)
    if y in list:
        print("GÓÓÓL !")
    else:
        print("Mimo brany")



root = tkinter.Tk()
root.geometry("480x346")

canvas = tkinter.Canvas(root,height=346, width=480)

img = ImageTk.PhotoImage(Image.open("ihrisko.png"))
img2 = ImageTk.PhotoImage(Image.open("lopta.png"))

canvas.create_image(0, 0, image=img, anchor="nw")
lopta = canvas.create_image(97, 165, image=img2, anchor="nw")
canvas.pack()
canvas.after(1000, move_ball)

root.mainloop()










