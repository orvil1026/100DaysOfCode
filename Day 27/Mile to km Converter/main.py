import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = int(input_in_miles.get())
    km = 1.609 * miles
    result.config(text=km)


label = tkinter.Label(text="is equal to")
label.grid(column=0, row=1)
label.config(padx=10, pady=10)

input_in_miles = tkinter.Entry(width=8)
input_in_miles.grid(column=1,row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

result = tkinter.Label(text="      ")
result.grid(column=1, row=1)

calculate = tkinter.Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1,row=2)

window.mainloop()