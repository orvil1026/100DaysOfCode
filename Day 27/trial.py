from tkinter import *

window = Tk()
window.title("Haha GUI")
window.minsize(width=600, height=600)
window.config(padx=100, pady=100)

label = Label(text="My label 1")
label.grid(column=0,row=0)


def label_shown():
    label.config(text=input.get())


button = Button(text="click me", command=label_shown)
button.grid(row=1, column=1)

button2 = Button(text="new_button", command=label_shown)
button2.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()