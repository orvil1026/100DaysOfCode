from tkinter import *
import pygame



# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LIGHTGREEN = "#a3ddcb"
DARKGREEN = "#314e52"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
ticks = ''
timer = None
# Sound Effect
# Sound Effect
pygame.mixer.init()


def play():
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play(loops=0)

# ---------------------------- TIMER RESET ------------------------------- #


def reset():

    global reps
    reps = 1
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    heading_label.config(text="Timer", fg=RED, bg=LIGHTGREEN)
    tick_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global ticks
    if reps == 8:
        heading_label.config(text="Break", fg=RED)
        count_timer = LONG_BREAK_MIN * 60
        ticks += "✔"

    elif reps % 2 == 0:
        heading_label.config(text="Break", fg=PINK)
        count_timer = SHORT_BREAK_MIN * 60
        ticks += "✔"
    else:
        heading_label.config(text="Work", fg=DARKGREEN)
        count_timer = WORK_MIN * 60
    play()
    if reps > 8:
        reps = 1
    reps += 1
    count_down(count_timer)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min_timer = count // 60
    sec_timer = count % 60

    if sec_timer < 10:
        sec_timer = '0' + str(sec_timer)

    canvas.itemconfig(timer_text, text=f"{min_timer}:{sec_timer}")
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global ticks
        tick_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=LIGHTGREEN,)
window.title("Pomodoro App")

canvas = Canvas(width=200, height=224, bg=LIGHTGREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(column=1, row=1)

heading_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=RED, bg=LIGHTGREEN)
heading_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), fg=DARKGREEN, bg=YELLOW, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"), fg=DARKGREEN, bg=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

tick_label = Label(font=(FONT_NAME, 15, "bold"), bg=LIGHTGREEN, fg=DARKGREEN)
tick_label.grid(column=1,row=3)

window.mainloop()