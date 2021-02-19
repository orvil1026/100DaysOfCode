import tkinter

window = tkinter.Tk()
window.title("My First GUI Program ")
window.minsize(width=500, height=500)

# Label

label = tkinter.Label(text="New label")
label.pack()


# Button

def label_shown():
    label.config(text=input_given.get())


button = tkinter.Button(text="Click me", command=label_shown)
button.pack()

# Entry

input_given = tkinter.Entry()
input_given.pack()

window.mainloop()