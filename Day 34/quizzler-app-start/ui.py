from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz:QuizBrain):
        self.quiz = quiz
        self.answer = True
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125,width=280, text='Welcome to Quizzler!',
                                                font=("Arial", 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.is_true)
        self.false_button = Button(image=false_img, highlightthickness=0,command=self.is_false)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text='Score=0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text=f'You have completed the quiz.\nYour Score is {self.quiz.score}/10')
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def is_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def is_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self,is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(ms=1000, func=self.next_question)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score:{self.quiz.score}/10")