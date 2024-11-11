import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "italic"))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Some Question Text",
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR,
                                                width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        tick_image = tk.PhotoImage(file="images/true.png")
        self.tick_button = tk.Button(image=tick_image, highlightthickness=0, command=self.right_answer)
        self.tick_button.grid(column=0, row=2)


        cross_image = tk.PhotoImage(file="images/false.png")
        self.cross_button = tk.Button(image=cross_image, highlightthickness=0, command=self.wrong_answer)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz.\n\n"
                                                       f"Your final score {self.quiz.score}/{self.quiz.question_number}")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def right_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


