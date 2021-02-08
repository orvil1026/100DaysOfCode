class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}:{question.text}(True/False)?")
        correct_answer = question.answer
        self.check_answer(answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("Thats wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f'Your current score is {self.score}/{self.question_number}\n')