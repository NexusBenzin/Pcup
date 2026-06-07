import tkinter, threading, time
from PIL import ImageTk, Image


def moving():
    time.sleep(1)
    while True:
        x0, y0 = canvas.coords(c0)
        x1, y1 = canvas.coords(c1)
        x2, y2 = canvas.coords(c2)
        x3, y3 = canvas.coords(c3)
        x4, y4 = canvas.coords(c4)

        canvas.moveto(c0, x1, y1)
        canvas.moveto(c1, x2, y2)
        canvas.moveto(c2, x3, y3)
        canvas.moveto(c3, x4, y4)
        canvas.moveto(c4, x0, y0)
        time.sleep(0.5)

Thread = threading.Thread(target=moving).start()


root = tkinter.Tk()
root.geometry("500x500")

canvas = tkinter.Canvas(root, background="white", width=300, height=300)
canvas.pack()

p0 = ImageTk.PhotoImage(Image.open("p0.png"))
p1 = ImageTk.PhotoImage(Image.open("p1.png"))
p2 = ImageTk.PhotoImage(Image.open("p2.png"))
p3 = ImageTk.PhotoImage(Image.open("p3.png"))
p4 = ImageTk.PhotoImage(Image.open("p4.png"))

c0 = canvas.create_image(0, 100, image=p0, anchor="nw")
c1 = canvas.create_image(50, 100, image=p1, anchor="nw")
c2 = canvas.create_image(100, 100, image=p2, anchor="nw")
c3 = canvas.create_image(150, 100, image=p3, anchor="nw")
c4 = canvas.create_image(200, 100, image=p4, anchor="nw")



root.mainloop()