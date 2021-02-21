from tkinter import *
from tkinter import messagebox
import random
import pyperclip3
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    numbers_list = [random.choice(numbers) for i in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for i in range(nr_symbols)]
    letters_list = [random.choice(letters) for i in range(nr_letters)]

    password_list = numbers_list + symbols_list + letters_list

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password


def on_click_password():
    password = generate_password()
    password_entry.insert(0,password)
    pyperclip3.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    final = website + '|| ' + email + '||' + password + '\n'

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error",message='Please do not leave the text box empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the entered details '
                                                              f'\nWebsite:{website},\nEmail:{email},\nPassword:{password}'
                                                              f' \nIs it ok?')
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(final)
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2,padx=10,pady=10)

email_entry = Entry(width=39)
email_entry.insert(0,"orvil@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2,padx=10,pady=10)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3,padx=10,pady=10)

generate_password_button = Button(text="Generate Password", command=on_click_password)
generate_password_button.grid(column=2, row=3,padx=10,pady=10)

add_button = Button(text="Add", width=35, command=save_data)
add_button.grid(column=1, row=4, columnspan=3,padx=10,pady=10)

window.mainloop()
