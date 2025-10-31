from question_model import Question
from data import question_data
from ui import TkQuiz

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

TkQuiz(question_bank)

