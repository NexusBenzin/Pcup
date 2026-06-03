import tkinter
import random
import time


root = tkinter.Tk()
root.geometry("300x300")

label = tkinter.Label(root, text="", font=("Arial", 72))
label.pack()

number = random.randint(10000,100000)
label.config(text=number)
time.sleep(1)
label.config(text="")



root.mainloop()

