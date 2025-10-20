
class QuestionBee:
    def __init__(self, q_number, q_list):
        self.q_number = q_number
        self.q_list = q_list
        self.counter = 1
        self.points = 0
        self.runs = 0


    def question_generator(self):
        import random
        self.q_number = random.randint(0, 11)
        current_question = self.q_list[self.q_number].question
        return(f"Q.{self.counter} is: {current_question} Is it (True or False)?")



    def analyze(self, answer):
        if answer == self.q_list[self.q_number].answer:
            print("Correct")
            self.counter += 1
            self.runs += 1
            self.points += 1
            print(f"Score: {self.points}/{self.runs}")
            return True


        else:
            print("Incorrect")
            self.counter += 1
            self.runs += 1
            self.points = self.points
            print(f"Score: {self.points}/{self.runs}")
            return True

    def game_over(self):
        if self.runs >= 7:
            return False

        else:
            return True

