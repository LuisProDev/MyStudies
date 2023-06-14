from question_model import *
from quiz_brain import *
from data import *

question_bank = []

for i in range(0, len(question_data)):
    question_bank.append(Question(question_data[i]["question"],
                                  question_data[i]["correct_answer"]))

quiz_brain = Brain(question_bank)

while quiz_brain.questions_remaining():
    quiz_brain.next_question()

print(f"You completed the quiz,"
      f" your final score was: {quiz_brain.score}/{quiz_brain.question_number}")

