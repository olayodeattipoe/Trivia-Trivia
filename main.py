from quiz_brain import Question
from data import question_data

print("Welcome to 2022 question trivia!\n")
score = 0

for i in range(len(question_data)):
    question = Question(i)
    marker = question.check_answer()
    if marker == 'true':
        score += 1
        print("Well done!")
        print(f"score = {score}/{len(question_data)}")
    elif marker == 'Wrong answer!':
        print("Mmm...Better luck on your next question.")
        print(f"score = {score}/{len(question_data)}")


