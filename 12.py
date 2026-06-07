import tkinter, random
from PIL import Image, ImageTk


def generate_positions():
    bx = random.randint(0, 500)
    by = random.randint(0, 500)
    kx = random.randint(500, 900)
    ky = random.randint(500, 800)

    def animate():
        b_x, b_y = canvas.coords(b1)
        b2 = None
        b3 = None
        def first():
            nonlocal b2
            canvas.delete(b1)
            b2 = canvas.create_image(b_x, b_y, image=balon2)

        def second():
            nonlocal b3
            canvas.delete(b2)
            b3 = canvas.create_image(b_x, b_y, image=balon3)

        def third():
            canvas.delete(b3)

        canvas.after(1000, first)
        canvas.after(2000, second)
        canvas.after(3000, third)


    def move():
        for i in range(10):
            canvas.move(b1, 20, 20)



        k_bbox = canvas.bbox(k)
        b_bbox = canvas.bbox(b1)

        bx1, by1, bx2, by2 = b_bbox
        kx1, ky1, kx2, ky2 = k_bbox

        h_overlap = bx1 < kx2 and bx2 > kx1
        v_overlap = by1 < ky2 and by2 > ky1

        if h_overlap and v_overlap:
            canvas.after(1, animate)
        else:
            canvas.after(1000, exit)




    canvas.moveto(k, kx, ky)
    canvas.moveto(b1, bx, by)
    canvas.after(3000, move)







root = tkinter.Tk()
root.geometry("1000x1000")

canvas = tkinter.Canvas(root, background="white", height=1000, width=1000)
canvas.pack()

balon1 = ImageTk.PhotoImage(Image.open("balon1.png"))
balon2 = ImageTk.PhotoImage(Image.open("balon2.png"))
balon3 = ImageTk.PhotoImage(Image.open("balon3.png"))
kaktus = ImageTk.PhotoImage(Image.open("kaktus.png"))

b1 = canvas.create_image(0, 0, image=balon1)
k = canvas.create_image(0, 0, image=kaktus)
canvas.after(1000, generate_positions)

root.mainloop()
