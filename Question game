from data import question_data

question_bank = []
answer_bank = []
question_index = []
counter = -1


for items in question_data:
    counter += 1
    question_bank.append(items['text'])
    answer_bank.append(items['answer'])
    question_index.append(counter)


class Question:

    def __init__(self, i):
        self.i = i

    def print_question_take_answer(self):
        result = input(f"Q.{self.i + 1}.{question_bank[self.i]} true/false? ").lower()
        return result

    def check_answer(self):
        user_answer = Question.print_question_take_answer(self)
        if user_answer == answer_bank[self.i].lower():
            return 'true'
        else:
            return 'Wrong answer!'
