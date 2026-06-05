import tkinter
import random


number = None
label = None
label2 = None

def check_answer():
    answer = input("Ake bolo moje cislo? ")
    if answer == str(number):
        label.config(text="SUPER")
    else:
        label.config(text="ZLE")
        label2.config(text=f"Bolo to {number}")

def remove_label():
    label.config(text="")
    root.after(100, check_answer)

root = tkinter.Tk()
root.geometry("300x300")

label = tkinter.Label(root, text="", font=("Arial", 60))
label.pack()

label2 = tkinter.Label(root, text="", font=("Arial", 24))
label2.pack()


number = random.randint(10000,100000)
label.config(text=number)

root.after(1000, remove_label)

root.mainloop()


