import tkinter

window = tkinter.Tk()
window.title("My First GUI Program ")
window.minsize(width=500, height=500)

label1 = tkinter.Label(text="New label")
label1.pack()

window.mainloop()