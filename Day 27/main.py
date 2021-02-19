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

#spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#scale


def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=50, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="is on?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

# radio buttons
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton2.pack()
radiobutton1.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ['Apple','Bananas','Orange','Pear']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()