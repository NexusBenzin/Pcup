import tkinter
import random
import time


root = tkinter.Tk()
root.geometry("300x300")

label = tkinter.Label(root, text="", font=("Arial", 72))
label.pack()

def clear_label():
    label.config(text="")

number = random.randint(10000,100000)
label.config(text=number)
label.after(1000, clear_label)




root.mainloop()

