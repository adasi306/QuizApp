from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank: list[Question] = []
for question in question_data:
    question_text: str = question["question"]
    question_answer: str = question["correct_answer"]
    new_question: Question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz: QuizBrain = QuizBrain(question_bank)
quiz_ui: QuizInterface = QuizInterface(quiz)