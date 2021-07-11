from tkinter import *
from projects.quizzler_application.quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizzlerInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx = 20, pady = 20)


        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR, pady = 10)
        self.score_label.grid(row = 0, column =2)

        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text((150, 125),
                                            text = f"sone text here",
                                            width = 275,
                                            fill = THEME_COLOR,
                                            font = ("Arial", 20, "italic"))
        self.canvas.grid(row = 1,column = 0, columnspan = 3, pady = 40)
        correct_image = PhotoImage(file = "images/true.png")
        wrong_image = PhotoImage(file = "images/false.png")
        self.correct_button = Button(image = correct_image, highlightthickness = 0, command = self.check_true)
        self.correct_button.grid(row = 2, column = 0)
        self.wrong_button = Button(image = wrong_image, highlightthickness = 0, command = self.check_false)
        self.wrong_button.grid(row = 2, column = 2)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz_brain.score}")
            ques_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text = ques_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end of the game")
            self.wrong_button.config(state = "disabled")
            self.correct_button.config(state="disabled")

    def check_true(self):
        result = self.quiz_brain.check_answer("True")
        self.show_effect(result)

    def check_false(self):
        result = self.quiz_brain.check_answer("False")
        self.show_effect(result)

    def show_effect(self, result):
        if result:
            self.canvas.config(bg = "green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)