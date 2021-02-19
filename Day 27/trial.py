from tkinter import *

window = Tk()
window.title("Haha GUI")
window.minsize(width=600, height=600)

label = Label(text="My label 1")
label.pack()


def label_shown():
    label.config(text=input.get())


button = Button(text="click me", command=label_shown)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()