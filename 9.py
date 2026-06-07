import tkinter, random
from PIL import Image, ImageTk



def random_number():
    same = True
    while same:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        if number1 != number2:
            same = False

        canvas.create_text(675, 300, text=str(number1), font=("Arial", 25))
        canvas.create_text(125, 300, text=str(number2), font=("Arial", 25))
        if number1 > number2:
            canvas.create_text(350, 100, text="Player on the right won!", font=("Arial", 25))
        elif number1 < number2:
            canvas.create_text(350, 100, text="Player on the left won!", font=("Arial", 25))




root = tkinter.Tk()
root.geometry("800x800")

canvas = tkinter.Canvas(root, width=800, height=800)
canvas.pack()
player_1 = ImageTk.PhotoImage(Image.open("jeseter.png"))
player_2 = ImageTk.PhotoImage(Image.open("shadow.png"))
referee = ImageTk.PhotoImage(Image.open("nexus.png"))

canvas.create_image(600, 400, image=player_1, anchor="nw")
canvas.create_image(50, 400, image=player_2, anchor="nw")
canvas.create_image(300, 200, image=referee, anchor="nw")
canvas.after(1000, random_number)



root.mainloop()