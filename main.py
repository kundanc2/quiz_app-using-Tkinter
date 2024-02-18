from question_model import Question
from data import question_data
from ui import QuizInterface
from quiz_brain import QuizBrain

question_bank = []

# saving question and correct_answer
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#creating object from QuizBrain class
quiz = QuizBrain(question_bank)

#creating object of QuizInterface class
new_interface=QuizInterface(quiz)
