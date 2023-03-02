from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
print("test")
#print(question_data[0]["text"])
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print("Unit test:")
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")