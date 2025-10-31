from tkinter import *
import html

THEME_COLOR = "#375362"


class TkQuiz:
    def __init__(self, questionbank):
        self.questionbank = questionbank
        self.score = 0
        self.q_number = 0

        # Window setup
        self.quizzer = Tk()
        self.quizzer.title("Quizzer by Ian Tristan")
        self.quizzer.config(width=450, height=600, bg=THEME_COLOR, padx=20, pady=20)

        # Score Label
        self.score_label = Label(
            text=f"Score: {self.score}",
            font=("Arial", 12, "bold"),
            bg=THEME_COLOR,
            fg="white"
        )
        self.score_label.place(x=300, y=20)

        # Question Canvas
        self.question_canvas = Canvas(
            self.quizzer,
            width=350,
            height=300,
            bg="white"
        )
        self.question_canvas.place(x=23, y=70)

        self.text = self.question_canvas.create_text(
            175,
            150,
            text="",
            font=("Arial", 20, "italic"),
            fill="black",
            width=300
        )

        # TRUE Button
        self.truePhoto = PhotoImage(file="./images/true.png")
        self.trueB = Button(image=self.truePhoto, command=self.true)
        self.trueB.place(x=20, y=450)

        # FALSE Button
        self.falsePhoto = PhotoImage(file="./images/false.png")
        self.falseB = Button(image=self.falsePhoto, command=self.false)
        self.falseB.place(x=275, y=450)

        # Load the first question
        self.next_question()

        self.quizzer.mainloop()

    # ---------------------------- NEXT QUESTION ------------------------------- #
    def next_question(self):
        if self.q_number < len(self.questionbank):
            q_text = html.unescape(self.questionbank[self.q_number].text)
            self.question_canvas.itemconfig(
                self.text,
                text=f"Q{self.q_number + 1}: {q_text}\n\n(True/False)?"
            )
        else:
            self.question_canvas.itemconfig(
                self.text,
                text=f"You’ve finished the quiz!\nFinal Score: {self.score}/{len(self.questionbank)}"
            )
            self.trueB.config(state="disabled")
            self.falseB.config(state="disabled")

    # ---------------------------- BUTTONS ------------------------------- #
    def true(self):
        self.check_answer("True")

    def false(self):
        self.check_answer("False")

    # ---------------------------- CHECK ANSWER ------------------------------- #
    def check_answer(self, user_answer):
        correct_answer = self.questionbank[self.q_number].answer
        if user_answer == correct_answer:
            self.score += 1
        self.q_number += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()
