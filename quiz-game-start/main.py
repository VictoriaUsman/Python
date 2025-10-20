import Logo
from question_model import Question_Up
from data import question_list
from quiz_brain import QuestionBee
import random

print(Logo.QandALOGO)
print("    Object Oriented Programming")
Question_Bank = []

for lines in question_list:
    question = lines["text"]
    answer = lines["answer"]
    Question_Bank.append(Question_Up(question, answer))

tanong_pa = True
randon_number = random.randrange(0, len(Question_Bank))
tanungan_na = QuestionBee(randon_number, Question_Bank)

while tanong_pa:
    sagot = input(tanungan_na.question_generator())
    tanungan_na.analyze(sagot)
    tanungan_na.game_over()
    if tanungan_na.game_over() == False:
        print("Game Over")
        tanong_pa = False




