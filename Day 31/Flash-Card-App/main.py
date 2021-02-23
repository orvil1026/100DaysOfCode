from tkinter import *
import pandas
import random
spanish = ''
english = ''
random_word_dict = {}
BACKGROUND_COLOR = "#B1DDC6"

# Importing data
data = pandas.read_csv("data-sheet.csv")
words_dict = data.to_dict(orient='records')


def get_random_dict():

    global spanish, english, timer, random_word_dict
    canvas.after_cancel(timer)
    random_word_dict = random.choice(words_dict)
    spanish = random_word_dict['Spanish']
    english = random_word_dict['English']
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_title, text='Spanish', fill='black')
    canvas.itemconfig(word_text, text=spanish, fill='black')
    timer = window.after(3000, flip)



def flip():

    global spanish, english
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_title, text="English",fill='white')
    canvas.itemconfig(word_text, text=english, fill='white')

# UI

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

timer = window.after(3000, flip)

card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
correct_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

canvas_image = canvas.create_image(400, 255, image=card_front)
canvas.grid(row=1, column=1, rowspan=2, columnspan=2)

language_title = canvas.create_text(400, 150, text='Spanish', font=("Arial", 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=("Arial", 60, 'bold'))
get_random_dict()

correct_button = Button(image=correct_img, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                        command=get_random_dict)

correct_button.grid(row=3, column=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR,
                      borderwidth=0, command=get_random_dict)

wrong_button.grid(row=3, column=2)

window.mainloop()