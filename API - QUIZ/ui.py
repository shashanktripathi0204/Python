from tkinter import *
from quiz_brain import QuizBrain
import subprocess


THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    # here we are telling quiz_brain that the data type that it is expecting is QuizBrain
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20., bg = THEME_COLOR)

        # Label
        # Score
        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        # canvas
        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        # Have to tell the canvas where to place the text here 150, 125
        self.question_text = self.canvas.create_text(
            150,
            125,
            text = "For Now",
            width=280, # word wrap
            fill=THEME_COLOR,
            font = (FONT_NAME, 20, "italic")
        )
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        # Button -> True
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(text = "", width = 100, height = 97, image = true_img,
                                  highlightthickness = 0, command = self.answer_true)
        self.true_button.grid(row = 2, column = 0)

        # Button -> False
        false_img = PhotoImage(file = "./Images/false.png")
        self.false_button = Button(text = "", width = 100, height = 97, image = false_img,
                                   highlightthickness = 0, command = self.answer_false)
        self.false_button.grid(row=2, column=1)


        # calling the get_next_question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "Reached the end of Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

            # Button -> reset
            self.reset_button = Button(text="Reset", width=20, height=2, pady = 10,
                                       highlightthickness=0, command=self.restart)
            self.reset_button.grid(row=3, column=0, columnspan = 2)


    def answer_false(self):
        return self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        return self.give_feedback(self.quiz.check_answer("True"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")

        else:
            self.canvas.config(bg = "red")
        self.window.after(400, self.get_next_question)

    def restart(self):
        self.window.destroy()
        subprocess.run(["python", "main.py"])
