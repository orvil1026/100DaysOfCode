from tkinter import *
from tkinter import messagebox
import random
import pyperclip3
import json
WHITE = '#d3e0ea'
LIGHTBLUE = '#a7c5eb'
BLUE = "#98ded9"
ORANGE = '#eb5e0b'

def search():
    website_entered = website_entry.get().lower()
    try:
        with open('data.json') as file:
            file_data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title='Error',message="No website found")

    else:
        if website_entered in file_data:
            email = file_data[website_entered]['email']
            password = file_data[website_entered]['password']
            messagebox.showinfo(title=website_entered, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showerror(title="Error", message='No website Found!')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get().lower()
    data = {
        website:{
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message='Please do not leave the text box empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the entered details '
                                                              f'\nWebsite:{website},\nEmail:{email},\nPassword:{password}'
                                                              f' \nIs it ok?')
        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    file_data = json.load(file)
                    file_data.update(data)

            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(data, file, indent=4)

            else:
                with open('data.json', mode='w') as file:
                    json.dump(file_data, file, indent=4)


            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=WHITE)

canvas = Canvas(width=200, height=200,bg=WHITE,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:',bg=WHITE)
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:',bg=WHITE)
email_label.grid(column=0, row=2)

password_label = Label(text='Password:',bg=WHITE)
password_label.grid(column=0, row=3)

website_entry = Entry(width=30)
website_entry.focus()
website_entry.grid(column=1, row=1, padx=10, pady=10)

email_entry = Entry(width=30)
email_entry.insert(0,"orvil@gmail.com")
email_entry.grid(column=1, row=2, padx=10, pady=10)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, padx=10, pady=10)

generate_password_button = Button(text="Generate Password", width=20, command=on_click_password, bg=LIGHTBLUE)
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

add_button = Button(text="Add", width=30, command=save_data, bg=BLUE)
add_button.grid(column=1, row=4, padx=10, pady=10)

search_button = Button(text="Search", width=20, command=search, bg=LIGHTBLUE)
search_button.grid(row=1, column=2)

window.mainloop()
