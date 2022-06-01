from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"))

        self.button_wrong = Button()
        self.button_wrong.config(image=false_img, highlightthickness=0, borderwidth=0, border=0, command=self.wrong_answer)
        self.button_wrong.grid(row=2, column=0)
        self.button_true = Button()
        self.button_true.config(image=true_img, highlightthickness=0, borderwidth=0, border=0, command =self.correct_answer)
        self.button_true.grid(row=2, column=1, pady=20)

        self.score_label = Label()
        self.score_label.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text =  self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions!")
            self.button_true.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong_answer(self):
       is_right =  self.quiz.check_answer("False")
       self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)