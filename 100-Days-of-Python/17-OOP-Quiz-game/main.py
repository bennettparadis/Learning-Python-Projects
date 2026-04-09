from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from random import shuffle

#Creates an empty list that will then be populated with Question objects
question_bank = []

for question in question_data:
    new_q = Question(question['text'], question['answer'])
    question_bank.append(new_q)

shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You answered all the questions!")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
