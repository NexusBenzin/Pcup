import tkinter, random, time
from idlelib.debugobj import make_objecttreeitem

score = 0


def move_square():
    x = random.randint(0, 720)
    y = random.randint(0, 720)
    canvas.moveto(square, x, y)
    root.after(800, move_square)


def mouse(*args):
        global score

        mouse_x = root.winfo_pointerx() - root.winfo_rootx()
        mouse_y = root.winfo_pointery() - root.winfo_rooty()

        overlap = canvas.find_overlapping(mouse_x, mouse_y, mouse_x, mouse_y)

        if square in overlap:
            score += 1
        else:
            score -= 2
        canvas.itemconfig(scores, text=f"Score: {score}")

root = tkinter.Tk()
root.geometry("800x800")

canvas = tkinter.Canvas(root, background="white", width=800, height=800)
canvas.pack()

square = canvas.create_rectangle(0, 0, 80, 80, fill="red")
scores = canvas.create_text(70, 50, text=f"Score: {score}", font=("Arial", 25))

root.bind("<ButtonPress-1>", mouse)
root.after(1000, move_square)

root.mainloop()
